from assistant.core import process_command
from assistant.recognizer import listen_for_command
from assistant.speaker import speak
from assistant.wakeword import is_wake_word_present

if __name__ == "__main__":
    speak("Hello! I'm Jarvis. Say 'Jarvis' followed by a command.")

    while True:
        query = listen_for_command()

        if query == "none":
            continue

        if is_wake_word_present(query):
            command = query.replace("jarvis", "").strip()
            if command in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            process_command(command)
        else:
            print("❗ Wake word not detected.")
