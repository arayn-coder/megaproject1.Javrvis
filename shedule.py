import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",160)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()




def my_schedule():
    schedule_list = []
    speak("Do you want to remove your old schedule? yes:-1, no:-2: ")
    user_input = int(input("Do you want to remove your old schedule? yes:-1, no:-2: "))
    speak("How many tasks should be added to your schedule? ")
    num_tasks = int(input("How many tasks should be added to your schedule? "))
    
    if user_input == 1:
        # Clear the existing file content
        with open("my_schedule.txt", "w") as file:
            file.write("")  # Empty the file
        
    # Add new tasks
    for i in range(num_tasks):
        task = input(f"Enter task {i+1} and time: ")
        schedule_list.append(task)
    
    # Write tasks to the file
    with open("my_schedule.txt", "a") as file:  # Use 'a' to append to the file
        for task in schedule_list:
            file.write(task + "\n")
    
    print("Tasks have been added to your schedule.")
    speak("Tasks have been added to your schedule.")



            
                 
    

