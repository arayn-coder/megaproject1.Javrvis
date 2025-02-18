from datetime import datetime
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()
def greet():
    while True:
        hour = int(datetime.now().hour)
        if hour>=0 and hour<=12:
            speak("Good morning, sir")

        elif hour>12 and hour<18:
            speak("good afternoon, sir")

        else:
            speak("good evening, sir")

        speak("Tell me sir, how can i help you!")
        break
