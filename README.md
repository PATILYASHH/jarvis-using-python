# Jarvis (Python Voice Assistant)

Jarvis is a voice-activated virtual assistant built using Python. It can recognize spoken commands, respond using text-to-speech, take notes, open local applications, search the web (Google, YouTube, Wikipedia, Stack Overflow, Amazon, Twitter, GitHub), interact with Gemini AI, and more. Say "Jarvis" followed by your command to get started!

---

## Features

- **Voice recognition** using your microphone
- **Text-to-speech** responses (using `pyttsx3`)
- **Take and show notes** with simple voice commands
- **Open local apps** (VS Code, Calculator, Chrome, File Explorer, etc.)
- **Search the web**: Google, Wikipedia, YouTube, Stack Overflow, Amazon, Twitter, and more
- **YouTube song search**
- **Weather search**
- **Integrates with Gemini AI** for advanced responses
- **Extensible**: Add your own commands easily!

---

## Installation

### Prerequisites

- Python 3.7 or above
- A working microphone

### Clone the Repository

```bash
git clone https://github.com/PATILYASHH/jarvis-using-python.git
cd jarvis-using-python
```

### Install Dependencies

The main dependencies are:

- `speechrecognition`
- `pyttsx3`
- `google-generativeai`
- `youtubesearchpython`

Install them using pip:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install:

```bash
pip install SpeechRecognition pyttsx3 google-generativeai youtubesearchpython
```

**Note:**  
- On Windows, you may need to install additional packages for microphone and audio support (e.g., `pyaudio`).  
- If you run into errors with `pyttsx3` or `pyaudio`, look for platform-specific solutions.

---

## Usage

1. **Configure Gemini API Key:**
   
   - Open `assistant/gemini.py`.
   - Replace the placeholder API key with your own [Gemini API key](https://ai.google.dev/).

2. **Run the Assistant:**

   ```bash
   python main.py
   ```

3. **Interact:**

   - Speak into your microphone.
   - Start every command with the wake word: **"Jarvis"** (e.g., "Jarvis, what's the weather?")
   - To exit, say: **"Jarvis exit"**, **"Jarvis quit"**, or **"Jarvis stop"**.

---

## Example Commands

- "Jarvis, what is the time?"
- "Jarvis, open VS Code"
- "Jarvis, search Google for Python tutorials"
- "Jarvis, play songs on YouTube"
- "Jarvis, remember buy milk"
- "Jarvis, show my notes"
- "Jarvis, open calculator"
- "Jarvis, what's the weather?"

---

## Project Structure

```
jarvis-using-python/
├── main.py                 # Entry point
├── assistant/
│   ├── core.py             # Command handling logic
│   ├── recognizer.py       # Speech recognition
│   ├── speaker.py          # Text-to-speech
│   ├── notes.py            # Notes management
│   ├── gemini.py           # Gemini AI integration
│   └── wakeword.py         # Wake word detection
├── requirements.txt        # Python dependencies (if present)
└── trial.py                # Miscellaneous script
```

---

## Extending Jarvis

To add your own commands, edit `assistant/core.py` and add logic inside the `process_command` function.

---

## Troubleshooting

- **Microphone Issues:** Make sure your microphone is working and set as the default device.
- **TTS Not Working:** Try running as administrator, or check your audio drivers.
- **Dependency Errors:** Ensure all Python dependencies are installed and up to date.

---

## Credits

- Developed by Yash Patil
- Gemini integration via [Google Generative AI](https://ai.google.dev/)

---

## License

This project is for personal and educational use.
