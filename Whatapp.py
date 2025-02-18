import pywhatkit
import datetime
from datetime import timedelta
from datetime import datetime
from time import sleep
import pyttsx3
import speech_recognition as sr
import sounddevice as sd
import wavio
import time
import os
import pyautogui as pg
import webbrowser
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

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for message...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return listen()  # Repeat listening
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return None

audio_filename = "voice_message.mp3"
def voice_recording(filename=audio_filename, duration=None, samplerate=44100):
    """Record voice and save it as a .wav file."""
    try:
        print("Recording started...")
        speak("Recording your message. Please speak.")
        audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=2, dtype='int16')
        sd.wait()  # Wait until recording is finished
        wavio.write(filename, audio, samplerate, sampwidth=2)
        print(f"Recording saved as {filename}")
        speak("Recording completed.")
    except Exception as e:
        print(f"Error during recording: {e}")
        speak("An error occurred during recording. Please try again.")

def send_voice_message(phonenumber):
   webbrowser.open(url="https://web.whatsapp.com/")
   time.sleep(10)
   pg.moveTo(x=219,y=234)
   pg.click()
   search = phonenumber
   pg.write(search)
   time.sleep(1)
   pg.press("Enter")
   pg.moveTo(x=716,y=971)
   pg.click()
   time.sleep(0.5)
   pg.moveTo(x=755,y=603)
   pg.click()
   time.sleep(1)
   pg.moveTo(x=96,y=406)
   pg.click()
   time.sleep(1)
   pg.hotkey("ctrl", "f")
   time.sleep(1)
   voice_path = audio_filename
   pg.write(voice_path)
   time.sleep(2)
   pg.moveTo(x=514, y=182)
   pg.click()   
   time.sleep(1)
   pg.press("Enter")
   time.sleep(1)
   pg.press("Enter")
   print("Your recording is send successfully")
   speak("Your recording is send successfully") 
   pg.hotkey("Alt", "F4")
# Current time for message scheduling
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

def Whatsapp_mode():
    """Main function to handle sending messages or recordings."""
    speak("Which person do you want to interact in your whatsapp?")
    user_input = int(input('''Choose a contact:
    1. Kunj Chaudhary
    2. Vishal Thakor
    3. Hardik Thakor

Enter your choice: '''))

    if user_input == 1:
        phone_number = "+919725558314"
    elif user_input == 2:
        phone_number = "+91 93272 92801"  # Replace with actual number
    elif user_input == 3:
        phone_number = "+91 97121 80171"  # Replace with actual number
    else:
        speak("Invalid choice.")
        return
    speak("What do you want to send? (Message, Voice Recording, Image")
    sent_category = input("What do you want to send? (Message-M, Voice Recording-V, Image-I): ").lower()
    if sent_category == "m":
        speak("What do you want to message?")
        message = listen()
        pywhatkit.sendwhatmsg(phone_number, message, time_hour=strTime, time_min=update)
        speak("Message scheduled.")
    elif sent_category == "v":
        speak("Take a time duration for recording: ")
        duration_time = int(input("Take a time duration for recording: "))
        voice_recording(duration=duration_time)
        send_voice_message(phonenumber=phone_number)

    elif sent_category == "i":
        speak("Enter the path of the image, you want to share")
        img_path = input("Enter the path of the image, you want to share: ")
        speak("You want write any caption related to image, (if no press enter)")
        img_caption = input(("You want write any caption related to image, (if no press enter): "))

        if img_caption == " ":
            img_caption = None
        else:
            pass
        pywhatkit.sendwhats_image(phone_number, img_path=img_path,caption=img_caption, wait_time=15,tab_close=True,close_time=3)
        speak("Image sent successfully")

    else:
        speak("Invalid category. Please choose again.")

