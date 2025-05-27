import google.generativeai as genai
from assistant.speaker import speak

genai.configure(api_key="AIzaSyCE9WGrYZ01X_L1U8YE3K4flleoSc9W1gc")

# Use a free-tier model instead of 'gemini-pro'
model = genai.GenerativeModel('gemini-1')

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        answer = response.text.strip()
        speak(answer)
        return answer
    except Exception as e:
        speak("Sorry, I couldn't get a response from Gemini.")
        print("Gemini error:", e)
        return None
