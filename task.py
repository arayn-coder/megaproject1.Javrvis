from datetime import datetime
import time
import pyttsx3
engine = pyttsx3.init()
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def add_task(task_name, task_time):
    """Add a task with the task name and reminder time."""
    task_list.append({"task": task_name, "time": task_time})

def check_tasks():
    """Check if it's time to remind the user of any tasks."""
    while True:
        now = datetime.now().strftime("%H:%M")
        # Iterate over a copy of the list to avoid modifying it while iterating
        for task in task_list[:]:
            if task["time"] == now:
                speak(f"Reminder: {task['task']}"*3)
                task_list.remove(task)  # Remove the task once reminded
        time.sleep(1)  # Check every minute

# Initialize task list as a list of dictionaries (not a list of lists)
task_list = []

# Adding tasks manually
add_task("it's time to some coding", "17:34")
add_task("Submit report", "18:09")
print(task_list)
print("waiting...")

# Start checking for tasks
check_tasks()