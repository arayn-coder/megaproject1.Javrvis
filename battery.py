import psutil
import pyttsx3
import speech_recognition as sr


recognizer = sr.Recognizer()  
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def Battery():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent

    if plugged:
        status = "Plugged In"
    else:
        status = "Unplugged"

    print(f"Battery Status: {status}")
    speak(f"Battery Status: {status}")
    print(f"Battery Percentage: {percent}%")
    speak(f"Battery Percentage: {percent}%")
