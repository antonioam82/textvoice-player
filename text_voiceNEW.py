import pyttsx3
from VALID import enum
import os
import sys

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',174)
text = ""
prev_text=""
listaV = engine.getProperty("voices")

print("*****************************************CHOOSE SPEAKER*****************************************")
op = enum(listaV)
engine.setProperty('voice',voices[listaV.index(op)].id)
os.system(var)


print(" _________")
print("|___   ___|")
print("    | | _____        _____               ______  __  ______  _____  ")
print("    | ||  ___|/\  /\|_   _|   /\      /\|  __  ||  ||  ____||  ___| ")
print("    | || |    \ \/ /  | | ____\ \    / /| |  | ||  || |     | |     ")
print("    | || >>>   \  /   | ||    |\ \  / / | |  | ||  || |     | >>>   ")
print("    | || |___  /  \   | ||____| \ \/ /  | |__| ||  || |____ | |___  ")
print("    |_||_____|/_/\_\  |_|        \__/   |______||__||______||_____| ")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------\n")

def speak(m):
    engine.say(m)
    engine.runAndWait()

while text != ".":
    text = input("TEXT: ")
    if text == " ":
        if prev_text == "":
            print("NO HAY TEXTO PREVIO",chr(7))
        else:
            print("REPITEIENDO AUDIO")
            speak(prev_text)
            
    else:
        speak(text)
        prev_text = text

