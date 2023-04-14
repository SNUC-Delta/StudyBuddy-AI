import speech_recognition as sr
from os import walk
r = sr.Recognizer()

def startConvertion(pathName): 
    try:
        with sr.AudioFile(pathName) as source:
            audio_file = r.record(source)
            output = r.recognize_google(audio_file, language='pt', show_all=True)
            return output["alternative"][0]['transcript']
    except TypeError:
        return "Speech not detected"

