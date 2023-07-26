import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# email = {"sanika":"sanikajoshi8903@gmail.com","aditi":"aditi25121978@gmail.com"}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour <= 0 and hour<12:
        speak("Good Morning!")
    elif hour>= 12 and hour <= 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello I am Jarvis. How may I help you?")

def takeCommand():
    ''' takes input from user in form of voice '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        #print(e)
        print("Say that again please..")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()


    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
                webbrowser.open("https://www.google.com/")

        elif 'open geeks for geeks' in query:
                webbrowser.open("https://www.geeksforgeeks.org/")

        elif 'open netflix' in query:
                webbrowser.open("https://www.netflix.com/in/")

        elif 'open linkedin' in query:
                webbrowser.open("https://www.linkedin.com/")

        elif 'open leet code' in query:
                webbrowser.open("https://leetcode.com/")

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

        elif 'open amazon music' in query:
                musicPath = "C:\\Users\\Sanika\\AppData\\Local\\Amazon Music\\Amazon Music.exe"
                os.startfile(musicPath)

        

        