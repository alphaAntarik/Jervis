
from numpy import take
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import subprocess as sp
import wikipedia
import webbrowser
import pywhatkit

#speak features-
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)
print(voices)
engine.setProperty('rate',170)

def speak(audio):
      print("  ")
      print(f": {audio}")
      print("  ")

      engine.say(audio)
      
      engine.runAndWait()

speak("Hello sir")

#wishme function
def wishme():
      hour =int(datetime.datetime.now().hour)
      if hour >=0 and hour <=12:
            speak("Good morning!")

      elif hour >12 and hour <=16:
            speak("Good afternoon!")

      else:
            speak("Good evening!")
      speak("Please tell me how can I help you!")
#take command 
def TakeCommand():

    
      r = sr.Recognizer()
      with sr.Microphone(device_index=1) as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

      try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
           
      except Exception as e:
            speak("Speak that again please...")
            return "None"
      return query

def youtube(term):
      result = "https://www.youtube.com/results?search_query="+term
      webbrowser.open(result)
      speak("There you go......")
      pywhatkit.playonyt(term)
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


if __name__ == "__main__":
      wishme()
      while True:
            query = TakeCommand().lower()

            #logic building for task
            if "open notepad" in query:
                  path = "C:\\Windows\\system32\\notepad.exe"
                  os.startfile(path)

            elif "open camera" in query:
                  open_camera()

            elif "wikipedia" in query:
                  speak('Searching wikipedia...')

                  query = query.replace("wikipedia","")
                  results = wikipedia.summary(query,sentences = 2)
                  speak("According to wikipedia")
                  speak(results)

            elif "open youtube" in query:
                  webbrowser.open("http://www.youtube.com/watch")

            elif "open google" in query:
                  webbrowser.open("google.com")

            elif "romantic songs" in query:
                  query = query.replace("jarvis","")
                  query = query.replace("play","")
                  youtube(query)

            elif "open stackoverflow" in query:
                  webbrowser.open("stackoverflow.com")

            


                 









