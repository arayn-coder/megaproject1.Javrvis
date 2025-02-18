import time
import datetime
import ctypes
import sys
import os
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def check(command):
    if "focus mode" in command.lower():
    
    


        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False  # Return False if we can't check for admin rights
        if is_admin():
            current_time = datetime.datetime.now().strftime("%H:%M")
            stop_time = input("Enter the time in [Hour:Minute] format: ")

            try:
                # Convert times to datetime objects for accurate comparison
                current_time_dt = datetime.datetime.strptime(current_time, "%H:%M")
                stop_time_dt = datetime.datetime.strptime(stop_time, "%H:%M")
            except ValueError:
                print("Invalid time format.")
                sys.exit()

            host_path = "C:\Windows\System32\drivers\etc\hosts"
            redirect = "127.0.0.1"
            website_list = []
            while True:
                user_input = input("Enter the website name you want to block and to exit press(e): ")
                if(user_input=="e"):
                    break
                else:
                    website_list.append(user_input)
            
            if current_time_dt <= stop_time_dt:
                with open(host_path, "r+") as file:
                    content = file.read()
                    for website in website_list:
                        if website not in content:
                          file.write(f"{redirect} {website}\n")
                    print(f"Entering focus mode...this Websites are blocked\n{website}.")
                    speak("Your distribution website are blocked!")
    
            # Continuously check the time to unblock websites after stop_time
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M")
                current_time_dt = datetime.datetime.strptime(current_time, "%H:%M")

                if current_time_dt >= stop_time_dt:
                    with open(host_path, "r+") as file:
                        content = file.readlines()
                        file.seek(0)
                        for line in content:
                            if not any(website in line for website in website_list):
                                file.write(line)
                        file.truncate()
                    print("Focus mode off. Websites unblocked.")
                    speak("Focus mode off. Websites unblocked!")
                    break
                time.sleep(1)  # Check every 1 seconds
        else:
            print("Admin privileges are required. Please run this script as administrator.")
            # Rerun the script with admin privileges if not already running as admin
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        pass


                