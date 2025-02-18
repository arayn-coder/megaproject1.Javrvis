import pyttsx3
import speech_recognition as sr
import requests

recognizer = sr.Recognizer()  
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_weather(command):
    api_key = "7917394eb7d10aec1e0edfc98d50184a"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {                # we use variable to pass dict for multiple imformation store
        'q': command,         # command parameter store city name
        'units': 'metric',
        'appid': api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["cod"] == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            result = (f"Weather in {command}: {weather}. "
                      f"Temperature: {temp}°C, Humidity: {humidity}%, "
                      f"Wind Speed: {wind_speed} meter per second.")
            speak(result)
            print(result)
            return result
        else:
            speak("City not found. Please check the city name and try again.")
            print("City not found. Please check the city name and try again.")
    except Exception as e:
        speak(f"An error occurred: {e}")
        print(f"An error occurred: {e}")


