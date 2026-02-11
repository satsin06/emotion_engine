import sounddevice as sd
import numpy as np
from emotion_engine.config import SAMPLE_RATE, AUDIO_DURATION

def record_audio() -> np.ndarray:
    audio = sd.rec(
        int(SAMPLE_RATE * AUDIO_DURATION),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()
    return audio.flatten()
