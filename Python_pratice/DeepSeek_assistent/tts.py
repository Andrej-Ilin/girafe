import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

def speak(text):
    threading.Thread(target=lambda: engine.say(text) and engine.runAndWait(), daemon=True).start()