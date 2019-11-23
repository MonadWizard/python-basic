import speech_recognition as sr
import winsound
freq = 2500
duration = 250
winsound.Beep(freq,duration)
r = sr.Recognizer()
with sr.Microphone() as source:
        audio = r.listen(source)
try:
    print (r.recognize_google(audio))
except:
    pass