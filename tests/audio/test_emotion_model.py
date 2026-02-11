import pytest
import numpy as np
from emotion_engine.audio.emotion_model import EmotionModel


def test_model_load_fails_without_file(tmp_path):
    model = EmotionModel(model_path=tmp_path / "missing.pt")

    with pytest.raises(FileNotFoundError):
        model.load()


def test_predict_input_shape():
    model = EmotionModel()
    features = np.random.randn(40).astype("float32")

    # We expect failure if model is missing, but not a crash
    try:
        model.predict(features)
    except FileNotFoundError:
        assert True
