import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty(
    "voice", voice[1].id
)  # 1 is for female voice and 0 is for male voice


def speak(content):
    print("FRIDAY: " + content)
    friday.say(content)
    friday.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    speak("Current time is: " + time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        # speak("What can I do for you?")
    elif hour >= 18 and hour < 24:
        speak("Good Evening!")
    speak("I am Friday Assistant. How may I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        c.pause_threshold = 1
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="vi-VN")
        print("User: " + query)
    except sr.UnknownValueError:
        speak("Please say again or input text or stop!")
        query = str(input("User: "))
    return query
#if any element of array in another array

def compare_string(input_string, array):
    max_similarity = 0
    result = ""
    for string in array:
        similarity = 0
        for i in range(len(input_string)):
            if i < len(string) and input_string[i] == string[i]:
                similarity += 1
        if similarity/len(string) > max_similarity:
            max_similarity = similarity/len(string)
            result = string
    return result

if __name__ == "__main__":
    # welcome()
    speak("Please tell me what you want to do")
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search on google")
            search = command().lower()
            url = "https://www.google.com/search?q=" + search
            wb.open(url)
            speak("Here is your search result for " + search)
        if "youtube" in query:
            speak("What should I search on youtube")
            search = command().lower()
            url = "https://www.youtube.com/results?search_query=" + search
            wb.open(url)
            speak("Here is your search result for " + search)
        if "open music" in query:
            folder_path = "D:\\Downloads\\Music"
            os.startfile(folder_path)
            #create list files in folder
            files = []
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    files.append(filename)
            speak("Tell me name of music you want to play")
            music = command().lower()
            #compare string music with list of files
            openmusic = compare_string(music, files)
            file_path = os.path.join(folder_path, openmusic)
            os.startfile(file_path)
            speak("Opening " + openmusic)
        if "time" in query:
            time()
        if "stop" in query:
            speak("Goodbye")
            break


