import time
import sounddevice as sd
import numpy as np
import librosa

from emotion_engine.audio.features import extract_mfcc, extract_pitch
from emotion_engine.audio.emotion_model import EmotionModel
from emotion_engine.fusion.combine import fuse
from emotion_engine.config import SAMPLE_RATE, AUDIO_DURATION


class EmotionEngine:
    def __init__(self):
        self.audio_model = EmotionModel()

    def analyze_microphone_stream(self):
        print("🎙 Listening... Press Ctrl+C to stop")

        try:
            while True:
                audio = sd.rec(
                    int(SAMPLE_RATE * AUDIO_DURATION),
                    samplerate=SAMPLE_RATE,
                    channels=1,
                    dtype="float32",
                )
                sd.wait()

                audio = audio.flatten()

                # Optional: silence gate
                if np.abs(audio).mean() < 0.005:
                    continue

                mfcc = extract_mfcc(audio)
                pitch = extract_pitch(audio)

                audio_emotion = self.audio_model.predict(mfcc)
                result = fuse(audio_emotion, {}, pitch)

                yield result

                time.sleep(0.1)

        except KeyboardInterrupt:
            print("\n🛑 Stopping microphone...")

        finally:
            # 🔑 HARD CLEANUP (very important)
            sd.stop()
            # sd.abort()
            print("🎤 Microphone released cleanly")

    def analyze_audio_file(self, file_path: str):

        audio, _ = librosa.load(file_path, sr=SAMPLE_RATE)
        mfcc = extract_mfcc(audio)
        pitch = extract_pitch(audio)

        audio_emotion = self.audio_model.predict(mfcc)
        result = fuse(audio_emotion, {}, pitch)

        return result
