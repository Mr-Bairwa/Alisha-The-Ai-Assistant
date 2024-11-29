import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
# import pyaudio
import os
import keyboard
import time
import pygame
import random
import subprocess
import pywhatkit as kit
from datetime import datetime, timedelta
# keyboard.press('space')
# keyboard.release('space')

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  

        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio) 
            print(data)
            return data            
            
        except sr.UnknownValueError:
            print(" not understand")
        
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

def play_music(data1):
    # Open YouTube and search for the query
    webbrowser.open(f"https://www.youtube.com/results?search_query={data1}")
    time.sleep(2) 
    # keyboard.press('space')
    # keyboard.release('space')


if __name__ == '__main__':
    
    
    while True:
            data1=sptext().lower()
            if 'your name' in data1:
                # name =" my name is Alisa"
                # speechtx(name)
                  speechtx(" my name is Alisa")
            
            elif 'I LOVE YOU' in data1:
                speechtx("I Love u too")

            elif 'how are you' in data1 or 'how r u' in data1:
                speechtx("I am doing great! Thank you for asking.")

            elif 'age' in data1 or 'year' in data1:
                age = "i am 10 day old"
                speechtx(age) 


            elif 'now time' in data1 or 'time' in data1:
                time=datetime.datetime.now().strftime("%I:%M %p") 
                speechtx(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")  
            elif 'amazon' in data1:
                webbrowser.open("https://www.amazon.com/")
            # elif 'Web Whatsapp' in data1:
            #     webbrowser.open("https://www.Webwhatsapp.com/")
            # elif 'open App' in data1:
            #   set_path="C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2445.7.0_x64__cv1g1gvanyjgm"
            #   subprocess.popen(set_path)

            elif 'play music' in data1 or 'play' in data1:

                choices = ['Millionaire' , 'Aaj Ki Raat', 'Russian Bandana']
                random_index = random.randint(0, len(choices) - 1)
                random_element = choices[random_index]

                print(f"Random Index: {random_index}")
                print(f"Element at Random Index: {random_element}")

                pygame.mixer.init()
                song_path = f"C:\Desktop\SONG\{choices[random_index]}.mp3"  
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                time.sleep(5)
                # while True:
                    # data2=sptext().lower()
            elif data1=='stop':
                pygame.mixer.music.stop() 
                        # break
                    # elif data2!="stop":
                        # data2=sptext().lower()
                # input("Say Stop Music to stop music")
                # continue
                     
            elif 'Message' in data1:
                All_Number={
                    'abhishek':'+919667609257',
                    'arun':'+919990984823',
                    'aditya':'+918882201619',
                    'angel':'+917310887499'
                }
                speechtx("name the person")
                data2= sptext().lower()
                phone_number = All_Number[f'{data2}']
                print(phone_number)
                message = 'Hello, this is a test message!'
                time = datetime.now()
                new_time = time + timedelta(seconds=60)
                Hours=int(new_time.strftime("%I "))
                Mins= int(new_time.strftime("%M "))
                print(Hours,Mins)
                kit.sendwhatmsg(phone_number, message, Hours,Mins)
                time.sleep(5)
                keyboard.press('enter')

            else :
                speechtx("sorry,i could not understand")
        



        