import typer
from emotion_engine.engine import EmotionEngine

app = typer.Typer()


@app.command()
def listen():
    """Listen continuously from microphone"""
    engine = EmotionEngine()

    for r in engine.analyze_microphone_stream():
        if r.get("silence"):
            continue  # keep listening silently

        typer.echo(f"\n📝 Text : {r['text']}")
        typer.echo(f"🎧 Audio Emotion : {r['audio']}")
        typer.echo(f"🧠 Text Emotion  : {r['text_emotion']}")
        typer.echo(f"🔀 Fused Emotion : {r['fused']}")

@app.command()
def file(path: str):
    """Analyze audio file"""
    engine = EmotionEngine()
    r = engine.analyze_audio_file(path)

    typer.echo(f"\n📝 Text : {r['text']}")
    typer.echo(f"🎧 Audio Emotion : {r['audio_emotion']}")
    typer.echo(f"🧠 Text Emotion  : {r['text_emotion']}")
    typer.echo(f"🔀 Fused Emotion : {r['fused_emotion']}")


def main():
    app()


if __name__ == "__main__":
    main()
