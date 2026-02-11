import numpy as np
import librosa
from emotion_engine.config import SAMPLE_RATE, N_MFCC

def extract_mfcc(audio: np.ndarray) -> np.ndarray:
    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=SAMPLE_RATE,
        n_mfcc=N_MFCC
    )
    mfcc = mfcc.mean(axis=1)
    mfcc = (mfcc - mfcc.mean()) / (mfcc.std() + 1e-6)
    return mfcc.astype("float32")


def extract_pitch(audio: np.ndarray) -> float:
    pitches, mags = librosa.piptrack(y=audio, sr=SAMPLE_RATE)
    pitch = pitches[mags > np.median(mags)]
    return float(pitch.mean()) if len(pitch) else 0.0
