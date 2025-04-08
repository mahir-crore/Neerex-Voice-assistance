import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI
import time 
import datetime
import numpy  as np
from gtts import gTTS
import pygame
import keyboard
import cv2 
import os
import pyautogui

# pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "9171485cc64f441998447ff7a6145493"
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
def aiProcess(command):
    client = OpenAI(api_key="<Enter Api Key >",
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named neerex skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if c.lower().startswith("open") or c.lower().startswith("start"):
        app = c.lower().split(" ", 1)[1]
        os.system(f"start {app}")
    elif "screenshot" in c.lower():
        time_str = time.strftime("%Y%m%d-%H%M%S")
        screenshot = pyautogui.screenshot()
        screenshot.save(f"screenshot_{time_str}.png")
        print(f"Screenshot saved as screenshot_{time_str}.png")
    elif c.lower().startswith("search") or c.lower().startswith("google"):
        query = c.split(" ", 1)[1]
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        webbrowser.open(search_url)
    elif "web" in c.lower():
        site = c.lower().split("web",1)[1].strip().split()[0] + ".com"
        webbrowser.open(site)
    elif "play" in c.lower() or "video" in c.lower():
        query = c.lower().replace("play", "").replace("video", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        time.sleep(6)
        pyautogui.click(522,275)
    elif "shutdown" in c.lower():
        os.system("shutdown /s /f /t 1")
        speak("Shutting down the system, goodbye!")
    elif "restart" in c.lower():
        speak("Restarting the system, please wait!")
        os.system("shutdown /r /f /t 1") 
    elif any(greet in c.lower() for greet in ["good morning", "good afternoon", "good evening", "good night"]):
        wish()
       
    elif "offline" in c.lower() or "exit" in c.lower():
        speak("Going offline. Have a good day!")
    elif  any(record  in c.lower() for record  in ["screen record", "record screen", "start screen recording"]):
        screen_record()
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()# Parse the JSON response
            articles = data.get('articles', [])  # Extract the articles
            for article in articles:# Print the headlines
                speak(article['title'])
    else:
        output = aiProcess(c)# Let OpenAI handle the request
        speak(output) 

def screen_record():
    print("Recording started... Press Ctrl + 9 to stop.")
    out = cv2.VideoWriter(
        f"screen_record_{time.strftime('%Y%m%d_%H%M%S')}.avi",
        cv2.VideoWriter_fourcc(*'XVID'),
        10,
        pyautogui.size()
    )

    while True:
        frame = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB)
        out.write(frame)
        if keyboard.is_pressed("ctrl+9"):
            print("Stopped.")
            break

    out.release()
def wish():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    elif hour <22:
        speak("Good Evening")
    else:
        speak("Good Night ")
    
    speak(f"Currently it is {time.strftime('%I:%M %p')}")
    speak("I am neerex. Online and ready sir. Please tell me how may I help you")

if __name__ == "__main__":
    speak("Initializing neerex....")
    while True:
        # Listen for the wake word "neerex"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() in ["suno", "start", "shur karo", "neerex"]:
                speak("ji ha bolo ")
                # Listen for command
                with sr.Microphone() as source:
                    print("neerex Active...")
                    while True:
                        try: 
                            audio = r.listen(source)
                            command = r.recognize_google(audio)
                            if command.lower() in ["exit", "stop", "back"]: 
                                speak("Okay sir, exiting command mode.")  
                                break  
                            processCommand(command)
                        except: 
                            print("Sorry, I didn't catch that.")  
                            speak("speak again ") 



        except Exception as e:
            print("Error; {0}".format(e))