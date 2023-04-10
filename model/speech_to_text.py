import speech_recognition as sr
from os import walk
file = "Server\output.wav"
r = sr.Recognizer()

def startConvertion(path = file): 
    try:
        with sr.AudioFile(path) as source:
            audio_file = r.record(source)
            output = r.recognize_google(audio_file, language='pt', show_all=True)
            return output["alternative"][0]['transcript']
    except TypeError:
        return "Speech not detected"
text = startConvertion()

print(text)