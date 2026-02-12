from collections import defaultdict

TEXT_TO_CANONICAL = {
    "joy": "happy",
    "surprise": "happy",
    "sadness": "sad",
    "anger": "angry",
    "disgust": "angry",
    "fear": "sad",
    "neutral": "neutral",
}

def normalize_text_emotions(text_probs: dict) -> dict:
    canonical = defaultdict(float)

    for label, score in text_probs.items():
        mapped = TEXT_TO_CANONICAL.get(label)
        if mapped:
            canonical[mapped] += score

    # normalize to sum = 1
    total = sum(canonical.values())
    if total > 0:
        for k in canonical:
            canonical[k] /= total

    return dict(canonical)
