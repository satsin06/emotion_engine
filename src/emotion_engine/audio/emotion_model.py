import torch
import numpy as np
from emotion_engine.audio.architecture import EmotionCNN
from emotion_engine.config import MODEL_PATH, EMOTIONS
from pathlib import Path

class EmotionModel:
    def __init__(self, model_path: Path = MODEL_PATH):
        self.model_path = model_path
        self.model = None

    def load(self):
        if self.model is not None:
            return self.model

        if not self.model_path.exists():
            raise FileNotFoundError(f"Emotion model not found at {self.model_path}")

        model = EmotionCNN(num_classes=len(EMOTIONS))
        state_dict = torch.load(self.model_path, map_location="cpu")
        model.load_state_dict(state_dict)
        model.eval()

        self.model = model
        return model

    def predict(self, mfcc: np.ndarray) -> dict[str, float]:
        model = self.load()

        with torch.no_grad():
            x = torch.tensor(mfcc).float().unsqueeze(0).unsqueeze(0)
            logits = model(x)
            probs = torch.softmax(logits, dim=1).squeeze().numpy()

        return {
            emotion: float(prob)
            for emotion, prob in zip(EMOTIONS, probs)
        }
