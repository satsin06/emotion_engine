import numpy as np
from emotion_engine.audio.mic import record_audio


def test_record_audio_shape(monkeypatch):
    def fake_rec(*args, **kwargs):
        return np.zeros((16000, 1), dtype=np.float32)

    monkeypatch.setattr("sounddevice.rec", fake_rec)
    monkeypatch.setattr("sounddevice.wait", lambda: None)

    audio = record_audio()
    assert isinstance(audio, np.ndarray)
    assert audio.ndim == 1
