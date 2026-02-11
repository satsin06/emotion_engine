from transformers import pipeline

class SentimentEngine:
    def __init__(self):
        self.pipe = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )

    def analyze(self, text: str) -> dict:
        result = self.pipe(text)[0]
        return {r["label"].lower(): r["score"] for r in result}
