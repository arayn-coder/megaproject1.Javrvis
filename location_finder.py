import speech_recognition as sr
import pyttsx3
import requests
from geopy.geocoders import Nominatim


# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Replace with your actual HERE Maps API key
API_KEY = "p6d10zFp2snyKfSoRnLmgxRZSlCwYRSRAP6IOZ3xVkI"

def get_current_location():
    """Get the current latitude and longitude using geopy."""
    try:
        geolocator = Nominatim(user_agent="Jarvis-Location-Finder")
        location = geolocator.geocode("Visnagar")  # Replace with your city or detect dynamically
        return location.latitude, location.longitude
    except Exception as e:
        print("Error fetching location:", e)
        return None, None

def find_nearby_places(keyword, latitude, longitude, radius=1000):
    """Find nearby places based on a keyword."""
    url = "https://discover.search.hereapi.com/v1/discover"
    params = {
        "q": keyword,  # Query keyword (e.g., "restaurant")
        "at": f"{latitude},{longitude}",  # Location as lat,lon
        "radius": radius,
        "apiKey": API_KEY,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print("Error fetching places:", response.status_code)
        return []

# Main Functionality
def location_finder():
    print("Welcome to Jarvis Location Finder!")
    speak("Welcome to Jarvis Location Finder!")
    
    latitude, longitude = get_current_location()
    
    if not latitude or not longitude:
        print("Unable to fetch your current location.")
        speak("Unable to fetch your current location.")
        return

    keyword = input("What are you looking for? (e.g., Italian restaurant, gas station): ")
    results = find_nearby_places(keyword, latitude, longitude)

    if results:
        print("\nHere are some nearby places:")
        speak("Here are some nearby places:")
        for i, place in enumerate(results[:5], 1):  # Limit to top 5 results
            name = place.get("title")  # Correct key for place name
            address = place.get("address", {}).get("label")  # Correct key for address
            print(f"{i}. {name} - {address}")
            speak(f"{i}. {name} - {address}")
    else:
        print("No nearby places found.")
        speak("No nearby places found.")

