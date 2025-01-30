import datetime as dt
import os
import smtplib
import subprocess
import sys
import time  # Import time module for sleep
import webbrowser

import pyttsx3
import pywhatkit as pk
import speech_recognition as sr
import wikipedia as wiki

listener = sr.Recognizer()  
speaker = pyttsx3.init()  

rate = speaker.getProperty('rate')  # getting details of current speaking rate  
speaker.setProperty('rate', 150)     # setting up new voice rate  

def speak(text):  
    speaker.say(text)  
    speaker.runAndWait()  

va_name = 'sobbuu'  

# Introduction function  
def introduce_virtual_assistant():  
    speak('hey this is ' + va_name)  # First part  
    time.sleep(0.5)                     # Pause for 1 second  
    speak('your virtual buddy.')       # Second part  
    time.sleep(0.5)                   # Pause for 0.5 second  
    speak('Tell me what to do.')      # Third part  

# Call the introduction function  
introduce_virtual_assistant()  

def take_command():  
    command = ''    
    try:  
        with sr.Microphone() as source:  
            print('Listening...')  
            voice = listener.listen(source)  
            command = listener.recognize_google(voice)  
            command = command.lower()  
            if va_name in command:  
                command = command.replace(va_name, '')  
    except Exception as e:  
        print('Check your microphone:', e)  
    return command  

def install_library(library_name):  
    """Installs a Python library using pip."""  
    try:  
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', library_name])  
        speak(f'{library_name} has been installed successfully.')  
    except subprocess.CalledProcessError as e:  
        print(f'An error occurred while installing {library_name}: {e}')  
        speak(f'An error occurred while installing {library_name}. Please check the console for more details.')  
    except Exception as e:  
        print(f'An unexpected error occurred: {e}')  
        speak('An unexpected error occurred. Please check the console for more details.')  

while True:  
    user_command = take_command()  
    print(user_command)  
    speak(user_command)  
    
    if 'close' in user_command:  
        print('See you again, Master Vishwa')  
        speak('See you again, Master Vishwa')  
        break  
    elif 'time' in user_command:  
        time = dt.datetime.now().strftime('%I:%M %p')  
        print(time)  
        speak(time)  
    elif 'play' in user_command:  
        user_command = user_command.replace('play', '')  
        print('Now playing ' + user_command)  
        speak('Now playing ' + user_command)  
        pk.playonyt(user_command)  
    elif 'search for' in user_command or 'google' in user_command:  
        user_command = user_command.replace('search for', '').replace('google', '')  
        print('Searching for ' + user_command)  
        speak('Searching for ' + user_command)  
        webbrowser.open('https://www.google.com/search?q=' + user_command)  
    elif 'who is' in user_command:  
        user_command = user_command.replace('who is', '')  
        summary = wiki.summary(user_command, sentences=5)  
        print(summary)  
        speak(summary)  
    elif 'who are you' in user_command:  
        print('I am Subuu, your virtual assistant')  
        speak('I am Subuu, your virtual assistant')  
    elif 'install' in user_command:  
        library_name = user_command.replace('install', '').strip()  
        if library_name:  
            print(f'Installing {library_name}...')  
            speak(f'Installing {library_name}...')  
            install_library(library_name)  
        else:  
            speak('Please specify the library name to install.')