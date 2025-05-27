def save_note(note):
    with open("jarvis_notes.txt", "a") as f:
        f.write(note + "\n")

def show_notes():
    try:
        with open("jarvis_notes.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "You have no notes yet."
