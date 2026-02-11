from emotion_engine import config


def test_sample_rate():
    assert config.SAMPLE_RATE > 0


def test_emotions():
    assert isinstance(config.EMOTIONS, list)
    assert len(config.EMOTIONS) > 0


def test_cache_dir_exists():
    assert config.CACHE_DIR.exists()
