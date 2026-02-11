def fuse(audio_probs: dict, text_probs: dict, pitch: float) -> dict:
    fused = {}

    for emotion in audio_probs:
        fused[emotion] = (
            0.6 * audio_probs.get(emotion, 0)
            + 0.4 * text_probs.get(emotion, 0)
        )

    # pitch heuristic
    if pitch > 180:
        fused["angry"] += 0.05
    elif pitch < 120:
        fused["sad"] += 0.05

    return fused
