import datetime
import webbrowser
import os
import difflib
from assistant.speaker import speak
from assistant.notes import save_note, show_notes
from assistant.gemini import ask_gemini
from youtubesearchpython import VideosSearch


def match_command(input_cmd, options):
    return difflib.get_close_matches(input_cmd, options, n=1, cutoff=0.6)

def process_command(command):
    command = command.lower()

    # Time and Date
    if any(kw in command for kw in ["time", "current time","what is time"]):
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
        return

    if any(kw in command for kw in ["date", "today's date","what is day"]):
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date}")
        return
    
    if any(kw in command for kw in ["what is date and time","what is time and date"]):
        time = datetime.datetime.now().strftime("%I:%M %p"),
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today Date is {date} and time is {time}")
        return

    # Notes
    if "remember" in command or "note" in command:
        if "show" in command:
            notes = show_notes()
            speak("Here are your notes.")
            print(notes)
        else:
            note = command.replace("remember", "").replace("note", "").strip()
            save_note(note)
            speak("Noted.")
        return
    # Notes and files from pc
    if "open python pdf" in command:
        speak("Opening python notes")
        os.startfile("D:\\download\\python notes cwh.pdf")
        return

    # YouTube song search
    if "play songs on youtube" in command or "play song" in command:
        term = command.replace("search youtube for", "").replace("youtube", "").strip()
        speak(f"Searching YouTube for your favorite songs")
        webbrowser.open(f"https://www.youtube.com/watch?v=xy3AcmW0lrQ")
        return

    # YouTube search
    if "youtube" in command:
        term = command.replace("search youtube for", "").replace("youtube", "").strip()
        speak(f"Searching YouTube for {term}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={term}")
        return

    # Google search
    if "google" in command or "search" in command:
        term = command.replace("search google for", "").replace("google", "").replace("search", "").strip()
        speak(f"Searching Google for {term}")
        webbrowser.open(f"https://www.google.com/search?q={term}")
        return

    # Wikipedia
    if "wikipedia" in command:
        term = command.replace("wikipedia", "").replace("search", "").strip()
        speak(f"Opening Wikipedia for {term}")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{term.replace(' ', '_')}")
        return

    # Amazon
    if "amazon" in command:
        term = command.replace("amazon", "").replace("search", "").strip()
        speak(f"Opening Amazon for {term}")
        webbrowser.open(f"https://www.amazon.in/s?k={term}")
        return

    # Stack Overflow
    if "stack overflow" in command:
        term = command.replace("stack overflow", "").replace("search", "").strip()
        speak(f"Searching Stack Overflow for {term}")
        webbrowser.open(f"https://stackoverflow.com/search?q={term}")
        return

    # GitHub
    if "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return

    # Twitter
    if "twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://twitter.com")
        return

    # Weather
    if "weather" in command:
        speak("Searching for weather info")
        webbrowser.open("https://www.google.com/search?q=current+weather")
        return

    if "remove chrome tab" in command:
        speak("Closing Chrome")
        os.system("taskkill /im chrome.exe")
        return
    
    # Chats handling 
    if "how are you" in command:
        speak("I am fine ,Thanks for asking"+ "How are you sir" )
        return
    
    if "fine"  in command:
        speak("Nice to here this."+ "How can i help you today" )
        return
    
    if "what is your name" in command:
        speak("My name is Jarvis , Created by Yash Patil")
        return
    
    # Apps

    if "open code" in command or "open vs code" in command:
        speak("Opning VS code")
        os.startfile("code")
        return
    
    if "open calculator" in command :
        speak("Opning Calculator")
        os.startfile("calc")
        return
    
    if "opne chrome" in command:
        speak("Opning google chrome")
        os.startfile("chrome")
        return

    if "Open file exporer" in command or "open files" in command:
        speak("Opning file explorer")
        os.startfile("explorer")
        return
    
        #websites
    if "opne portfolio website" in command or "open my website" in command:
        speak("Opening your website")
        webbrowser.open("https://yashpatil.tech")
        return
    
    if "canvas" in command:
        speak("Opning exeldraw in chrome")
        webbrowser.open("https://excalidraw.com/")
        return
    

   

    # Fallback
    speak("Let me search that for you...")
    webbrowser.open(f"https://www.google.com/search?q={command}")
