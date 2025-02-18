import pyttsx3
import speech_recognition as sr


recognizer = sr.Recognizer()  
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)

def speak(text):
    """Convert text to speech."""
    
    engine.say(text)
    engine.runAndWait()



class Calculator:
    
    def __init__(self, command):
        self.command = command

    def square(command):
        result = command * command
        speak(f"The square is {result}")
        print(f"The square is {result}")
        return result
    
    def cube(command):
        result = command * command * command
        speak(f"The cube is {result}")
        print(f"The cube is {result}")

        return result
    
    def squareroot(command):
        result = command ** 0.5
        speak(f"The square root is {result}")
        print(f"The square root is {result}")
        return result

