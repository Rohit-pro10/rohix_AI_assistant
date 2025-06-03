import speech_recognition as sr
import webbrowser
import pyttsx3
import music_Library
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
        
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
       speak("playing song....")
       song =c.lower().split(" ")[1]
       link = music_Library.music[song]
       webbrowser.open(link)
       
    
if __name__ =="__main__":

    speak("initialize rohi.....")

    #listen the word "jarvis"
    # obtain audio from the Microphone
    while True:
        r = sr.Recognizer() 
        print("Recognizing.....")


        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                command = r.recognize_google(audio)
            print(command)
            if(command.lower()=="rohit"):
                speak("yes sir ji")
                # listen for command
                with sr.Microphone() as source:
                     print("rohix active.....")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     processCommand(command)

            
        except Exception as e:
            print(" error : {0}".format(e))





