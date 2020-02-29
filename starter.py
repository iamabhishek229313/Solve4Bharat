import pyttsx3
import os 
import pytesseract 
import speech_recognition as sr 
language = 'en'
custom_config = r'--oem 3 --psm 6'

#Intializing the Speech Recognition 
r = sr.Recognizer()



#Speaking Engine
defaultRate = 180
engine = pyttsx3.init()
engine.setProperty('rate',defaultRate)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def saySomething(text,rate):
    engine.setProperty('rate' , rate)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate',defaultRate)

def heyListen(duration):
    with sr.Microphone() as source :
        print("Listening....")
        audio_data = r.record(source,duration = duration)
        text = r.recognize_google(audio_data)
        return text

saySomething("Hi dear , What's your Name ?",180) 
saySomething("Hello " + heyListen(5),130)
saySomething("Should I start device as enviroment mode for you ?" , 150)
selectedMode = heyListen(5)
if selectedMode == "yes" :
    saySomething("Okay , we are going to enviroment mode ", 130)
    exec(open('./Smart_wear.py').read())
elif selectedMode == "no" :
    saySomething("Ok  , See you have a nice day !",130)

engine.stop()