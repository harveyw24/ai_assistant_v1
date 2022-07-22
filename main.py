'''
Author: Harvey
Date: 2022-07-21 18:58:22
LastEditors: Harvey
LastEditTime: 2022-07-22 02:04:03
Description: 
'''
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio

engine = pyttsx3.init() # microsoft text to speech engine

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning!")
        print("Hello, Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon!")
        print("Hello, Good Afternoon!")
    else:
        speak("Hello, Good Evening!")
        print("Hello, Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"User: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant G-One.")
speak("Loading your AI personal assistant G-One.")
wishMe()

def main():
    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        # TODO: Use "connect()" in pyttsx3, wrapper function for speak/print
        if "goodbye" in statement or "okay bye" in statement or "stop" in statement:
            speak('Your personal assistant G-one is shutting down, goodbye.')
            print('Your personal assistant G-one is shutting down, goodbye.')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        time.sleep(1)

if __name__ == '__main__':
    main()