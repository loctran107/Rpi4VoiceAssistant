import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from os import path
from time import gmtime, strftime

#Speak function
def speak(test):
    tts = gTTS(text=test, lang='en')
    if path.exists("voice.mp3"):
        os.remove("voice.mp3")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(str(e))
    return said
            
if __name__ == '__main__':
    text = getaudio()
    #Check and respond
    if "Giovanni" in text:
        speak("Welcome back, Donavan")
        while 1:
            command = getaudio()
            if "music" in command:
                speak("I'm playing music")
            if "time" in command:
                speak(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
            if "quit" in command:
                break
    
    