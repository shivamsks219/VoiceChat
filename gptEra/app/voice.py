import pyttsx3
import speech_recognition as sr


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            speechtx("Please try Again ")
            return -1

def speechtx(x):
    z=1
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[z].id)
    rate = engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()



