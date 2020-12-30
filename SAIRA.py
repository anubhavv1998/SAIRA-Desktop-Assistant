from tkinter import *
import tkinter as tk
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import winshell
import requests
import wolframalpha
import pywhatkit as pwt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = tk.Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        var.set("Hello ! Good Morning Anubhav")
        window.update()
        speak("Hello ! Good Morning Anubhav!")
    elif 12 <= hour <= 18:
        var.set("Hello ! Good Afternoon Anubhav!")
        window.update()
        speak("Hello ! Good Afternoon Anubhav!")
    else:
        var.set("Hello ! Good Evening Anubhav")
        window.update()
        speak("Hello ! Good Evening Anubhav!")
    speak("Myself SAIRA! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        speak("Pardon me, please say that again")
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='green')
    wishme()
    while True:
        btn1.configure(bg='dark blue')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            speak("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open movies' in query:
            var.set("Opening Movies")
            window.update()
            speak("Opening Movies")
            os.startfile("D:\\Movies")

        elif 'open software' in query:
            var.set("Opening Software")
            window.update()
            speak("Opening Software")
            os.startfile("D:\\Software")

        elif 'series' in query:
            var.set("Opening OTD Series")
            window.update()
            speak("Opening OTD Series")
            os.startfile("E:\\OTD")

        elif 'code' in query:
            var.set("Opening V S Code")
            window.update()
            speak("Opening V S Code")
            os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        elif ('play music' in query) or ('music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'C:\\Users\\Lenovo\\Music\\Audio'
            songs = os.listdir(music_dir)
            n = random.randint(0, 71)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I %M %S %p")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "calculate" in query:  
            app_id = "PTW6PG-X63YYGTL6W"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("PTW6PG-X63YYGTL6W")
            res = client.query(query)
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
                speak('No results found')

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        elif ('old are you' in query) or ('version' in query):
            var.set("Version 0.1.1 ")
            window.update()
            speak("I am a newbie sir ! Version 0.1.1")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            os.startfile("C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe")

        elif 'your name' in query:
            var.set("Myself SAIRA")
            window.update()
            speak("Myself SAIRA")

        elif 'weather' in query:
            api_key = "659d4ba65a35ab7af4a4a6926062d70e"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'on youtube' in query:
            song = query.replace('play','')
            var.set('Playing on Youtube')
            speak('playing'+song)
            pwt.playonyt(song)

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
                stream.release()

        elif 'who made you' in query:
            var.set("My Creator is Anubhav Singh")
            window.update()
            speak("My Creator is Anubhav Singh")

        elif 'open python' in query:
            var.set("Opening Python")
            window.update()
            speak("Opening Python")
            os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\python.exe")

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open sublime' in query:
            var.set('Opening Sublime')
            window.update()
            speak('opening Sublime')
            os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")

        elif 'open anaconda' in query:
            var.set('Opening Anaconda')
            window.update()
            speak('opening anaconda')
            os.startfile("C:\\Users\\Lenovo\\anaconda3\\python.exe")

        elif 'sleep' in query:
            var.set('Sleeping...............')
            window.update()
            speak("OK Anubhav!! time to sleep have a good day")
            quit()


def update(ind):
    frame = frames[ind % 10]
    ind += 1
    label.configure(image=frame)
    window.after(10, update, ind)


label2 = Label(window, textvariable=var1, bg='#730cfa')
label2.config(font=("Fixedsys", 30))
var1.set('YOU SAID:')
label2.pack(pady=10)

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Fixedsys", 20))
var.set('Welcome')
label1.pack()

# noinspection PyRedundantParentheses
frames = [PhotoImage(file='SAIRA.gif', format='gif -index %i'% (i)) for i in range(10)]
window.title('SAIRA by Anubhav')
window.iconbitmap(r'iipsicon.ico')

label = Label(window, width=500, height=150)
label.pack(pady=135) 
window.after(0, update, 0)


def mode1():
    window.configure(bg='black')


def mode2():
    window.configure(bg='#f0f0f0')


btn0 = Button(text='SAY HI', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='START', width=20, command=play, bg='DARK BLUE')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='QUIT', width=20, command=window.destroy, bg='RED')
btn2.config(font=("Courier", 12))
btn2.pack()
btn3 = Button(window, text='DARK MODE', width=20, command=mode1, bg='Black', fg='White')
btn3.config(font=("Courier", 12))
btn3.pack()
btn4 = Button(window, text='LIGHT MODE', width=20, command=mode2, fg='Black', bg='WHITE')
btn4.config(font=("Courier", 12))
btn4.pack()

window.mainloop()
