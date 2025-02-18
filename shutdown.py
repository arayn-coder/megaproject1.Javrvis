import speech_recognition as sr
import pyttsx3
import os

recognizer = sr.Recognizer()  
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice command and convert it to text."""
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")
            return command
    except sr.UnknownValueError:
        speak("Command not received clearly!")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet.")
        return None

def shut_down():
    """Shutdown the system after user command."""
    speak("Are you sure you want to shut down your system?")
    print("Do you want to shut down your system? Say 'definitely jarvis' or 'no jarvis'.")
    command = listen()
    if command and ("definitely" in command and "jarvis" in command):
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif command and ("no" in command and "jarvis" in command):
        speak("Shutdown canceled.")
    else:
        speak("I didn't understand that. Please say 'definitely jarvis' or 'no jarvis'.")

