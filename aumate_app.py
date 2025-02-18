import webbrowser
import pyautogui
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def pause_start(command):
    command = command.replace("jarvis", "")
    pyautogui.hotkey("k")
    if "stop" in command.lower():
        speak("ok,pauseing the video!")

    else:
        speak("ok,start the video!")

def scroll_down(steps=300):
    """Scrolls down by the specified number of steps."""
    pyautogui.scroll(-steps)  # Negative value for scrolling down
    speak("OK, scrolling down!")
    pyautogui.sleep(2)

# Function to scroll up
def scroll_up(steps=300):
    """Scrolls up by the specified number of steps."""
    pyautogui.scroll(steps)   # Positive value for scrolling up
    speak("ok, scrolling up!")
    pyautogui.sleep(2)

def click_video(command):
    pyautogui.click()
    command = command.replace("click", " ")
    command = command.replace("the", " ")
    command = command.replace("jarvis", " ")
    speak(f"ok, clicking the {command}!")

def full_screen():
    pyautogui.hotkey("f")
    speak("ok, full screen the video!")
    pyautogui.sleep(1)

def search(command):
    while True:
        if "search" in command.lower():
            command = command.replace("search", "")
            command = command.replace("jarvis", "")
            pyautogui.hotkey("/")
            pyautogui.write(command)
            pyautogui.press("enter")
            speak(f"ok, searching the {command}")
            pyautogui.moveTo(x=644, y=402)
            pyautogui.sleep(1)
        else:
            pass
        break
   
def close_tab():
    pyautogui.hotkey("ctrl","w")
    speak("close tab!")
    pyautogui.sleep(1)
# def test():
#     pyautogui.moveTo(644, 402)

# test()