import random
import pyttsx3
import speech_recognition as sr

# Initialize pyttsx3 for Jarvis to speak
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice command function to get the player's choice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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

# Game function
def Game():

    while True:
        jarvis_choice = random.choice([1, 2, 3])
    
        speak("Please choose Stone, Paper, or Scissors.")
        youstr = listen()

        if youstr is None:
            return

        # Dictionary for mapping words to game choices
        youdic = {"stone": 1, "paper": 2, "scissors": 3}
        reversedic = {1: "stone", 2: "paper", 3: "scissors"}

        if youstr not in youdic:
            speak("Invalid choice, please choose between Stone, Paper, or Scissors.")
            return

        # Get the user's choice based on spoken command
        you = youdic[youstr]
        print(f"You chose {reversedic[you]}, Computer chose {reversedic[jarvis_choice]}")

        # Speak out the choices
        speak(f"You chose {reversedic[you]}, Computer chose {reversedic[jarvis_choice]}")

        # Determine the result
        if jarvis_choice == you:
            speak("It's a draw!")
        elif (jarvis_choice == 1 and you == 3) or (jarvis_choice == 3 and you == 2) or (jarvis_choice == 2 and you == 1):
            speak("You lose, try again!")
            speak("do you want to play another round")
            
            
        else:
            speak("You win!")

        speak("do you want to play another round!")
        command = listen()
        command = command.replace("jarvis", " ")
        if(command !="yes"):
            break
def guessing_game():
    import random
    n = random.randint(1, 100)

    a = -1
    guesses = 1
    while(a != n):
        a = int(input("Guess the number: "))
        if(a>n):
            print("Lower number please")
            speak("Lower number please")
            guesses +=1

        elif(a<n):
            print("Higher number please")
            speak("Higher number please")
            guesses +=1

    print(f"You gussed the number {n} correctly in {guesses} attempts")
    speak(f"You gussed the number {n} correctly in {guesses} attempts")

def main_game():
    speak("Which game you want to play!")
    choice_game = int(input("Which game you want to play [for stone, paper, scissor-1 and guesseing the number-2]: "))

    if choice_game==1:
        speak("let's paly stone, paper, scissor!")
        Game()

    elif choice_game==2:
        speak("let's play guessing the guess number")
        guessing_game()

    else:
        print("No game available")
        speak("No game available")
