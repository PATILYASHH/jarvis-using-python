import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis 🔊: {text}")
    engine.say(text)
    engine.runAndWait()
