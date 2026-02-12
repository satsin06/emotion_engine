from typing import Dict

TEXT_TO_AUDIO = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "neutral": "neutral",
    "fear": "neutral",
    "surprise": "neutral",
    "disgust": "angry",
}

AUDIO_EMOTIONS = ["happy", "sad", "angry", "neutral"]


def fuse(
    audio_probs: Dict[str, float],
    text_probs: Dict[str, float],
    *,
    text_weight: float = 0.7,
    audio_weight: float = 0.3,
) -> Dict[str, float]:
    fused = {e: 0.0 for e in AUDIO_EMOTIONS}

    # 1️⃣ Map text emotions → audio space
    for text_emotion, score in text_probs.items():
        mapped = TEXT_TO_AUDIO.get(text_emotion)
        if mapped:
            fused[mapped] += text_weight * score

    # 2️⃣ Add audio emotion directly
    for emotion in AUDIO_EMOTIONS:
        fused[emotion] += audio_weight * audio_probs.get(emotion, 0.0)

    # 3️⃣ Normalize (soft)
    total = sum(fused.values())
    if total > 0:
        fused = {k: v / total for k, v in fused.items()}

    return fused
