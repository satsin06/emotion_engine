import time
import tempfile
import sounddevice as sd
import numpy as np
import librosa
import soundfile as sf

from emotion_engine.audio.features import extract_mfcc, extract_pitch
from emotion_engine.audio.emotion_model import EmotionModel
from emotion_engine.text.asr import ASREngine
from emotion_engine.text.sentiment import SentimentEngine
from emotion_engine.fusion.combine import fuse
from emotion_engine.config import SAMPLE_RATE, AUDIO_DURATION


class EmotionEngine:
    def __init__(self):
        # Audio emotion
        self.audio_model = EmotionModel()

        # Text engines
        self.asr_engine = ASREngine()
        self.sentiment_engine = SentimentEngine()

    def analyze_microphone_stream(self):
        """
        Continuous mic → audio emotion + text emotion → fusion
        Yields results indefinitely
        """
        print("🎙 Listening... Press Ctrl+C to stop")

        buffer = []
        buffer_duration = 0.0
        block_duration = 0.3  # seconds
        silence_threshold = 0.001

        try:
            with sd.InputStream(
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype="float32",
                blocksize=int(SAMPLE_RATE * block_duration),
            ) as stream:

                while True:
                    audio, _ = stream.read(stream.blocksize)
                    audio = audio.flatten()

                    energy = np.sqrt(np.mean(audio**2))
                    print(f"🔊 Mic energy: {energy:.6f}")

                    # Silence → keep listening, don't stop mic
                    if energy < silence_threshold:
                        time.sleep(0.05)
                        continue

                    # Accumulate speech
                    buffer.append(audio)
                    buffer_duration += block_duration

                    # Process every AUDIO_DURATION seconds
                    if buffer_duration < AUDIO_DURATION:
                        continue

                    full_audio = np.concatenate(buffer)
                    buffer.clear()
                    buffer_duration = 0.0

                    # ===== AUDIO EMOTION =====
                    mfcc = extract_mfcc(full_audio)
                    pitch = extract_pitch(full_audio)
                    audio_emotion = self.audio_model.predict(mfcc)

                    # ===== ASR =====
                    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
                        sf.write(tmp.name, full_audio, SAMPLE_RATE)
                        text = self.asr_engine.transcribe(tmp.name)

                    # ===== TEXT EMOTION =====
                    text_emotion = (
                        self.sentiment_engine.analyze(text)
                        if text.strip()
                        else {}
                    )

                    # ===== FUSION =====
                    fused = fuse(
                        audio_probs=audio_emotion,
                        text_probs=text_emotion,
                        text_weight=0.7,
                        audio_weight=0.3,
                    )

                    yield {
                        "text": text,
                        "audio": audio_emotion,
                        "text_emotion": text_emotion,
                        "fused": fused,
                    }

        except KeyboardInterrupt:
            print("\n🛑 Stopped listening")

    def analyze_audio_file(self, file_path: str):
        audio, _ = librosa.load(file_path, sr=SAMPLE_RATE)

        mfcc = extract_mfcc(audio)
        pitch = extract_pitch(audio)
        audio_emotion = self.audio_model.predict(mfcc)

        text = self.asr_engine.transcribe(file_path)
        text_emotion = (
            self.sentiment_engine.analyze(text)
            if text.strip()
            else {}
        )

        fused = fuse(
            audio_probs=audio_emotion,
            text_probs=text_emotion,
            text_weight=0.7,
            audio_weight=0.3,
        )

        return {
            "text": text,
            "audio_emotion": audio_emotion,
            "text_emotion": text_emotion,
            "fused_emotion": fused,
        }

