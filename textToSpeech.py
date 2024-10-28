import pyttsx3

engine = pyttsx3.init()
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.say("Test text, read this.") # her skal output fra index leses opp fra output.txt
engine.runAndWait()