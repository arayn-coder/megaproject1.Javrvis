
from time import sleep
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
import pygame
import time


pygame.mixer.init()

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def translng(command):
    speak("Sure, sir!")
    print(LANGUAGES)
    translator = Translator()
    speak("Choose a language in which you want to translate")
    
    # Language input
    language_input = input("Which language: ").strip().lower()
    
    # Check if language is valid
    if language_input not in LANGUAGES.values():
        speak("Sorry, that language is not supported.")
        return
    
    # Translate the text
    language_code = [code for code, lang in LANGUAGES.items() if lang == language_input][0]
    text_to_translate = translator.translate(command, src="auto", dest=language_code)
    text = text_to_translate.text
    
    try:
        # Convert translated text to speech
        speaklg = gTTS(text=text, lang=language_code, slow=False)
        speaklg.save("voice.mp3")
        
        # Play the audio
        pygame.mixer.music.load("voice.mp3")
        pygame.mixer.music.play()
        
        # Wait for the playback to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)  # Wait in small increments
            
        # Stop and unload the file
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
        # Delete the audio file
        os.remove("voice.mp3")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, this language is not supported by the text-to-speech engine.")
