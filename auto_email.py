import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import pyttsx3
import speech_recognition as sr

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

def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path=None):
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body text
        msg.attach(MIMEText(body, 'plain'))

        # Attach a file if provided
        if attachment_path and os.path.exists(attachment_path):
            attachment = MIMEBase('application', 'octet-stream')
            with open(attachment_path, 'rb') as file:
                attachment.set_payload(file.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(attachment)
        elif attachment_path:
            print("Attachment file not found!")
            speak("Attachment file not found!")

        # Connect to the SMTP server
        print("Connecting to SMTP server...")
        speak("Connecting to SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")
        speak("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("Failed to send email!")

    