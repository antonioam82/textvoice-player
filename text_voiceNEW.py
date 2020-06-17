import pyttsx3
from VALID import enum

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
text = ""
prev_text=""
listaV = engine.getProperty("voices")

print("******************************ESTABLECE SPEAKER******************************")
op = enum(listaV)
engine.setProperty('voice',voices[listaV.index(op)].id)


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
            print("NO HAY MENSAJE ANTERIOR",chr(7))
        else:
            print("REPITIENDO MENSAJE")
            speak(prev_text)
            
    else:
        speak(text)
        prev_text = text

