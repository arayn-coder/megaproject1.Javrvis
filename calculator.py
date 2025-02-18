import pyttsx3
import speech_recognition as sr
import wolframalpha
recognizer = sr.Recognizer()  
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def wolfram_alpha(command):
    """Query Wolfram Alpha and return the result."""
    apikey = "H8P739-EXJUAJH7ER"
    client = wolframalpha.Client(apikey)
    
    try:
        response = client.query(command)
        answer = next(response.results).text
        return answer
    except StopIteration:
        speak("Sorry, sir. Your value is not answerable!")
        return None

def calculate(command):
    """Process and calculate a spoken arithmetic command."""
    # Normalize the command
    term = command.lower()
    term = term.replace("jarvis", "")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("into", "*")
    term = term.replace("divid", "/")
    term = term.replace("calculate", "")
    term = term.replace("square of", "**2")



    try:
        # Get the result from Wolfram Alpha
        result = wolfram_alpha(term)
        if result:
            speak(f"The result of {command} equal to {result}")
            print(f"The result of {command} = {result}")
        else:
            speak("I couldn't compute that. Please try again.")
    except Exception as e:
        speak("Sorry, I couldn't process your request.")
        print(f"Error: {e}")


    

    
