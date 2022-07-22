'''
Author: Harvey
Date: 2022-07-21 18:58:22
LastEditors: Harvey
LastEditTime: 2022-07-22 03:47:44
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

import config

engine = pyttsx3.init() # microsoft text to speech engine

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greetMe():
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
greetMe()

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

        # skill: wikipedia search
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # skill: web browser actions
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is open now")
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Email is open now")
        elif 'news' in statement:
            webbrowser.open_new_tab("https://www.nytimes.com")
            speak('Here are some headlines from the New York Times.')
        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)

        # skill: current time
        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%l:%M %p")
            speak(f"The time is {strTime}")
        elif 'date' in statement:
            strDate = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f'The date is {strDate}')

        # skill: camera
        # TODO: delete that photo!
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"G-One Camera","g-one-img.jpg")
        
        # skill: wolfram alpha
        elif 'ask' in statement:
            speak('What question do you want to ask me?')
            question = takeCommand()
            client = wolframalpha.Client(config.WOLFRAM_APP_ID)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        # skill: self-identity
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O, your personal assistant. I am programmed to perform minor tasks like'
                  'opening youtube, telling time, taking a photo, searching wikipedia, or sharing the weather forecast.' 
                  'You can ask me computational or geographical questions too!')
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Harvey")
            print("I was built by Harvey")

        time.sleep(1)

if __name__ == '__main__':
    main()