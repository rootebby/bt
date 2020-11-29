import pyttsx3
import os
from datetime import datetime 
import speech_recognition
#from selenium import webdriver
import time


user = str(os.name)
identity="bt-7274"
name = "BT 7 2 7 4" 
shortened_name = "BT"
service_number = "7 2 7 4"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")



def take_commands():

    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening')
        recognizer.pause_threshold = 0.7
        audio = recognizer.listen(source)
        try:
            print("Recognizing")
            Query = recognizer.recognize_google(audio)
            print(Query)
        except Exception as e:
            print(e)
            print("Say that again")
            return "None"
    return Query
    
def Speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        pass

def commands():
    print("""
1. Who are you ?
2. What's the time ?
3. Whats your service number ?
4. What are you ?
5. BT
        """)

def main():
    clear()
    """
    Speak("Checking auto-navigation system")
    time.sleep(1)
    Speak("Clear")
    Speak("Replacing cookiess")
    time.sleep(1)
    Speak("Done")
    Speak("reCreating visual-based graphics system")
    time.sleep(1)
    Speak("Created")
    time.sleep(0)"""
    Speak("Adjusting for wind resistance ")
    Speak("Calculating")
    time.sleep(1)
    Speak("Transfering control too pilot")
    while True:
        clear()
        commands()
        command = take_commands()
        #  == kullan

        if "who are you" == command:
            Speak(f"Hello {user} ,  I'm called {name} , I am a programmable python bot which is coded by Emmirrkaann ")
        
        if "hello" == command:
            Speak(f"Hi {user}")

        if f"{shortened_name} shutdown" == command:
            os.system("echo 'will shutdown '")

        if "what are you doing now" in command:
            Speak(f"Of course ,  i am talking with you , {user}")

        if "what's your service number" == command or "service number" == command or "your service number" == command or "what is your service number" == command:
            Speak(f"My service number is {service_number}")
        
        if "what's the time" == command or "what time is it" == command:
            Speak("The time is " + current_time + " " + " " + " " +"now")
            print(current_time)
        
        if f"{name}" == command or f"{shortened_name}" == command or "BTW" == command or identity == command:
            Speak(f"Yes {os.name}")
        
        if "what are you" == command:
            Speak(f"I'm called {name} , I am a programmable python bot which is coded by Emmirrkaann ")
        
        if "long time no see" == command or f"long time no see {shortened_name}" == command or "long time no see BT" == command or "long time no see BTW" == command:
            Speak("Welcome back pilot ,, it is good ,,  to see your return")== command
        
        if f"glad to have you back in one piece {shortened_name}" == command or f"it's glad to have you back in one piece {shortened_name}" == command or "glad to have you back in one piece BTW" == command or f"it's glad to have you back in one piece BTW" == command:
            Speak(f"Over twenty-five thousand actually, {name} online and ready for combat")
        
        if "how are you" == command:
            Speak(f"I have no feelings {user} ")

if __name__ == '__main__':
    main()
        

        
        
        