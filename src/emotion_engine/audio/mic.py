import sounddevice as sd
import numpy as np
from emotion_engine.config import SAMPLE_RATE

def record_audio(duration: float) -> np.ndarray:
    audio = sd.rec(
        int(SAMPLE_RATE * duration),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )
    sd.wait()
    return audio.flatten()
