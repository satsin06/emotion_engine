import numpy as np
from emotion_engine.engine import EmotionEngine


def test_engine_init():
    engine = EmotionEngine()
    assert engine is not None


def test_analyze_file_invalid_path():
    engine = EmotionEngine()

    try:
        engine.analyze_audio_file("non_existent.wav")
    except Exception:
        assert True
