import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
        except:
            return "none"

    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
        return query.lower()
    except:
        return "none"
