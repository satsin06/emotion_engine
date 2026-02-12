import time
from emotion_engine.engine import EmotionEngine

RECORD_SECONDS = 3
PAUSE_SECONDS = 0.5


def run_continuous_text_emotion():
    engine = EmotionEngine()

    print("\n🎤 Continuous mic → ASR → text emotion")
    print("⏹️ Press Ctrl+C to stop\n")

    try:
        for result in engine.analyze_microphone_stream():
            print("📝 Text :", result["text"])
            print("🧠 Text Emotion :", result["text_emotion"])
            print("-" * 40)
            time.sleep(PAUSE_SECONDS)

    except KeyboardInterrupt:
        print("\n🛑 Stopped")


if __name__ == "__main__":
    run_continuous_text_emotion()
