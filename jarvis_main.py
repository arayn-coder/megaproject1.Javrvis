import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import os
from datetime import datetime
import time
import threading
import musicLibrary 
import greetME
import subprocess
import calculator
import battery
import game
import weather
import caculator_2
import shutdown
from plyer import notification
import pygame
import pyautogui
import pygetwindow as gw
import aumate_app
import volume_control
import auto_email
import pyjokes




# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()                    
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)

# Task list to store reminders
task_list = []

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def add_task(task_name, task_time):
    """Add a task with the task name and reminder time."""
    task_list.append({"task": task_name, "time": task_time})
    file = open("task.txt","w")
    file.write(str(task_list))
    file.close()

def check_tasks():
    """Check if it's time to remind the user of any tasks."""
    while True:
        now = datetime.now().strftime("%H:%M") 
        for task in task_list[:]:
            if task["time"] == now:
                speak(f"Reminder:,it's time to some {task['task']}!"*3)
                task_list.remove()  
        time.sleep(1)  # Check every 1 seconds

def process_command(command):
    """Process the command received."""
    print(f"Command received: {command}")
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "whatsapp buddy" in command.lower():
        speak("Perfect, sir")
        speak("tell me Whats'about you!")
    elif "i am also perfect" in command.lower():
        speak("that's great, sir!")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("Opening YouTube.")
    elif "close youtube" in command.lower():
        if os.name == "nt":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing the youtube.")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "close facebook" in command.lower():
        if os.name == "nt":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing the facebook.")
    elif "close instagram" in command.lower():
        if os.name == "nt":
            os.system("taskkill /f /im msedge.exe")
            speak("Closing the instagram.")
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")

    elif "open github" in command.lower():
        path = "C:\\Users\\tkrar\\Desktop\\GitHub Desktop.lnk"
        os.startfile(path)
        speak("opening the github")
    elif "close github" in command.lower():
        subprocess.call(['taskkill', '/F', '/IM', 'GitHubDesktop.exe'])
        speak("GitHub Desktop has been closed!")

    elif "joke" in command.lower():
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
        

    elif "find location" in command.lower():
        from location_finder import location_finder
        location_finder()
    
    elif "whatsapp mod" in command.lower():
        from Whatapp import Whatsapp_mode
        Whatsapp_mode()   

    elif "send email" in command.lower():
        speak("Enter your email address")
        sender_email = input("Enter your email address: ")
        speak("Enter your email password (or app password)")
        sender_password = input("Enter your email password (or app password): ")
        speak("Enter recipient email address")
        recipient_email = input("Enter recipient email address: ")
        speak("Enter the subject")
        subject = input("Enter the subject: ")
        speak("Enter the email body")
        body = input("Enter the email body: ")
        speak("Enter the path of the attachment (leave blank for no attachment)")
        attachment_path = input("Enter the path of the attachment (leave blank for no attachment): ").strip()

        if attachment_path == '':
            attachment_path = None
        
        auto_email.send_email_with_attachment(sender_email=sender_email, sender_password=sender_password, recipient_email=recipient_email, subject=subject, body=body, attachment_path=attachment_path)
     
    elif "generate qr code" in command.lower():
        import qr_generating
        speak("ok, generating qrcode!")
        qr_generating.QR_code()
      
    elif "search" in command.lower():
        aumate_app.search(command)

    elif "stop" in command.lower():
        aumate_app.pause_start(command)
    
    elif "focus mode" in command.lower():

        speak("Are you sure you want, on a focus mode!")
        user_input = int(input("Are you sure you want on a focus mode![1 for yes 2 for no]: "))
        if(user_input == 1):
            speak("Entering the focus mode!")
            import FocusMode
            FocusMode.check(command)
            exit()
        else:
            speak("canceling the focus mode")

    elif "start" in command.lower():
        aumate_app.pause_start(command)

    elif "scroll down" in command.lower():
        aumate_app.scroll_down()

    elif "scroll up" in command.lower():
        aumate_app.scroll_up()

    elif "click" in command.lower():
        aumate_app.click_video(command)

    elif "full" in command.lower():
        aumate_app.full_screen()

    elif "volume up" in command.lower():
        volume_control.volume_up()          # volume up to 10%

    elif "volume down" in command.lower():
        volume_control.volume_down()        # volume down to 10%

    elif "translate" in command.lower():
        from transalator import translng
        command = command.replace("jarvis", "")
        command = command.replace("translate", "")
        translng(command)

    elif "calculate" in command.lower():
        command = command.replace("calculate", "")
        command = command.replace("jarvis", "")
        calculator.calculate(command)

    elif "weather in" in command.lower():
        command = command.replace("weather in", "")
        command = command.replace("jarvis", "")
        weather.get_weather(command) 

    elif "cube of" in command.lower():
        command = command.replace("what is", "" )
        command = command.replace("cube of", "")    
        command = command.replace("jarvis", "")
        caculator_2.Calculator.cube(int(command))

    elif "square of" in command.lower():
        command = command.replace("square of", "")
        command = command.replace("jarvis", "")
        caculator_2.Calculator.square(int(command))

    elif "square root" in command.lower():
        command = command.replace("square root", "")
        command = command.replace("of", " ")
        command = command.replace("what", " ")
        command = command.replace("is", " ")
        command = command.replace("calculate", "")
        caculator_2.Calculator.squareroot(int(command))

    elif "shutdown" in command.lower():   #Ensure the projecet is open in command prompnt
        shutdown.shut_down()

    elif "close tab" in command.lower():
        aumate_app.close_tab()

    elif "open" in command.lower():
        command = command.replace("open", "")
        command = command.replace("jarvis", "")
        try:
            pyautogui.press("super")
            
            pyautogui.typewrite(command)
            pyautogui.press("Enter")
            speak(f"opening the {command}!")

        except:
            speak(f"{command} is not found in your system!")

    elif "close" in command.lower():
        command = command.replace("close", "")
        command = command.replace("jarvis", "")
        try:
            pyautogui.hotkey("Alt", "F4")
            pyautogui.sleep(1)
            speak(f"Closing the {command}!")
        except:
            speak(f"sorry, {command} is not open")


    elif "play a game" in command.lower():
        game.main_game()
        
    
    elif "battery status" in command.lower():
        battery.Battery()

    elif "make my schedule" in command.lower():
        from shedule import my_schedule
        my_schedule()

    elif "show my task" in command.lower():
        task_file = open("task.txt", "r")
        content = task_file.read()
        print(content)
        task_file.close()
        pygame.mixer.init()
        pygame.mixer.music.load("music.wav")
        pygame.mixer_music.play()
        notification.notify(
            title = "My Task:-",
            message = content,
        )

    elif "show my schedule" in command.lower():
        task_file = open("my_schedule.txt", "r")
        content = task_file.read()
        print(content)
        task_file.close()
        pygame.mixer.init()
        pygame.mixer.music.load("music.wav")
        pygame.mixer_music.play()
        notification.notify(
            title = "My Schedule:-",
            message = content,
        )

    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=a349b46d84a04f0e8e82b49cb73819c0")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles[:5]:  # Read top 5 headlines
                    headline = article.get('title')
                    if headline:
                        speak(headline)
            else:
                speak("I couldn't find any news at the moment.")
    elif command.lower().startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music[song]
        if song in musicLibrary.music:
            musicLibrary.music.get(link)
            webbrowser.open(link)

        else:
           speak("Sorry, the song is not found in your list, sir!")     
             
    elif "time" in command:
        now = datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}.")
        
    elif "date" in command:
        today = datetime.today().strftime("%d/%m/%Y")
        speak(f"Today's date is {today}.")

    elif "add my task" in command:
        speak("Please state the task and time.")
        try:
            print("listening for task...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=5)
                task_command = recognizer.recognize_google(audio).lower()
                print(task_command)
                task_command = task_command.replace("my", "")
                task_command = task_command.replace("is", "")
                task_command = task_command.replace("jarvis", "")
                # Parsing task and time from the command
                task_name = task_command.split("task ")[1].split(" at ")[0]  #formate is, you speak task then they add task name and you speak at then they add time.
                task_time = task_command.split(" at ")[1]
                add_task(task_name, task_time)
            
                speak(f"Task '{task_name}' added for {task_time}.")
                print(f"{task_name} {task_time}")
        except IndexError:
            speak("Sorry, I couldn't understand the task format.")
        except sr.UnknownValueError:
            speak("I couldn't hear the task clearly.")
            
def start_task_manager():
    """Start the task manager in a separate thread."""
    task_thread = threading.Thread(target=check_tasks)
    task_thread.daemon = True
    task_thread.start()

# Main program loop to listen for the wake word and commands
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    # Start task manager
    start_task_manager()

    is_active = False  # Flag to track if Jarvis is active

    while True:
        try:
            with sr.Microphone() as source:
                if not is_active:
                    print("Listening for wake word...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                    try:
                        word = recognizer.recognize_google(audio).lower()
                        print(f"Heard: {word}")
                        
                        if "jarvis" in word:
                            greetME.greet()
                            
                            
                            is_active = True  # Activate Jarvis
                            
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand the audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Speech Recognition service; {e}")
                
                if is_active:
                    print("Jarvis is active. Listening for command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                    try:
                        command = recognizer.recognize_google(audio).lower()
                        print(f"Command: {command}")
                        
                        if "go to sleep" in command:
                            speak("Going to sleep, sir but you call me any time!.")
                            exit()  # Deactivate Jarvis
                        else:
                            process_command(command)  # Handle the command
                            

                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand the audio.")
                    except sr.RequestError as e:
                        print(f"Could not request results from Google Speech Recognition service; {e}")
                    except sr.WaitTimeoutError:
                        print("Listening timed out.")

        except sr.WaitTimeoutError:
            print("Listening timed out.")
        except Exception as e:
            print(f"An error occurred: {e}")
