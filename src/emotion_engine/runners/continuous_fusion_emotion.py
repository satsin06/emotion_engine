# src/emotion_engine/runners/continuous_mic_fusion_emotion.py
import time
from emotion_engine.engine import EmotionEngine

PAUSE_SECONDS = 0.5


def run_continuous_fusion():
    engine = EmotionEngine()

    print("\n🎤 Continuous mic → audio + text → fusion")
    print("⏹️ Press Ctrl+C to stop\n")

    try:
        for result in engine.analyze_microphone_stream():
            print("🎧 Audio Emotion :", result["audio_emotion"])
            print("🧠 Text Emotion  :", result["text_emotion"])
            print("🔀 Fused Emotion :", result["fused_emotion"])
            print("-" * 50)
            time.sleep(PAUSE_SECONDS)

    except KeyboardInterrupt:
        print("\n🛑 Stopped")


if __name__ == "__main__":
    run_continuous_fusion()
