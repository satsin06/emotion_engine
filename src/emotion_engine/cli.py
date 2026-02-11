import typer
from emotion_engine.engine import EmotionEngine

app = typer.Typer()


@app.command()
def listen():
    """Listen continuously from microphone"""
    engine = EmotionEngine()
    for result in engine.analyze_microphone_stream():
        typer.echo(result)

@app.command()
def file(path: str):
    """Analyze audio file"""
    engine = EmotionEngine()
    result = engine.analyze_audio_file(path)
    typer.echo(result)

def main():
    app()

if __name__ == "__main__":
    main()
