import numpy as np
from emotion_engine.audio.features import extract_mfcc, extract_pitch
from emotion_engine.config import SAMPLE_RATE


def fake_audio():
    return np.random.randn(SAMPLE_RATE).astype(np.float32)


def test_extract_mfcc():
    mfcc = extract_mfcc(fake_audio())
    assert isinstance(mfcc, np.ndarray)
    assert mfcc.ndim == 1


def test_extract_pitch():
    pitch = extract_pitch(fake_audio())
    assert isinstance(pitch, float)
    assert pitch >= 0.0
