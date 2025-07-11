import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Nói đi nào...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="vi-VN")
    print("✅ Bạn đã nói:", text)
except sr.UnknownValueError:
    print("❌ Không nghe rõ.")
except sr.RequestError as e:
    print(f"❌ Lỗi kết nối Google Speech API: {e}")
