from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
Listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')        #for changign the voice type     
engine.setProperty('voice',voices[1].id)      # this line is also used in changing the voice type.

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
     try:
        with sr.Microphone() as source:
            print("listening...")
            voice = Listener.listen(source)
            command = Listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
     except:
        pass
     return command
def run_alexa():
        command = take_command()
        print(command)
        if 'play'in command:
            song = command.replace('play','')
            talk('playing'+ song) 
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time  = datetime.datetime.now().strftime('%H:%M %p')
            talk('current time is'+ time)
            print(time)
        elif 'screenshot'in command:
            talk('taking scrrenshot')
            pywhatkit.take_screenshot()
        #elif 'google' in command:
           # talk('opening google')
            #pywhatkit.open_web('https://www.google.com')
        elif 'find' in command:
            person = command.replace('find','')
            info = wikipedia.summary(person,1)
            print(info)
            talk(info)  
        elif 'hay jack' in command:
            talk('hello ankit,i am fine, how are you')
            print(talk())
        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())
        else :
            talk('say it again')


        
while True:
    run_alexa()