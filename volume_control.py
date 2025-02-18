from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

# Initialize audio interface
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Function to increase volume
def volume_up(step=0.1):
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current_volume + step, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume increased to {new_volume * 100:.0f}%")
    speak(f"Volume increased to {new_volume * 100:.0f}%")
    
# Function to decrease volume
def volume_down(step=0.1):
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current_volume - step, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume decreased to {new_volume * 100:.0f}%")
    speak(f"Volume decreased to {new_volume * 100:.0f}%")
