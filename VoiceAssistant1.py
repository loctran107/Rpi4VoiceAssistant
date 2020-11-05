import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

#Speak function
def speak(test):
    tts = gTTS(text=test, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    #os.remove("voice.mp3")

def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))
    return said
            
if __name__ == '__main__':
   # speak("Hello")
    #while 1:
    text = getaudio()

    #Check and respond
    if "Lee" in text:
        speak("Nice to meet you Donavan")
    else:
        speak("Something")
    
    
     