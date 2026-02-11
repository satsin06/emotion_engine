from pathlib import Path

SAMPLE_RATE = 16_000
N_MFCC = 40
AUDIO_DURATION = 3.0

EMOTIONS = ["neutral", "happy", "sad", "angry"]

CACHE_DIR = Path.home() / ".cache" / "emotion-engine"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = CACHE_DIR / "emotion_model.pt"
