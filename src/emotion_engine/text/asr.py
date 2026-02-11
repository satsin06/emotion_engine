from faster_whisper import WhisperModel

class ASREngine:
    def __init__(self, model_size="small"):
        self.model = WhisperModel(model_size, device="cpu")

    def transcribe(self, audio_path: str) -> str:
        segments, _ = self.model.transcribe(audio_path)
        return " ".join(seg.text for seg in segments)
