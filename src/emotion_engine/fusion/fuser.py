def fuse_emotions(audio, text, alpha=0.6):
    fused = {}
    for k in audio:
        fused[k] = alpha * text.get(k, 0) + (1 - alpha) * audio.get(k, 0)

    # normalize
    total = sum(fused.values())
    for k in fused:
        fused[k] = round(fused[k] / total, 2)

    return dict(sorted(fused.items(), key=lambda x: x[1], reverse=True))
