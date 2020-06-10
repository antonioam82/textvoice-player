import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
text = ""
prev_text=""

print("*ESTABLECE IDIOMA*")
print("A)-ESPAÑOL--------")
print("B)-INGLÉS---------")

while True:
    op = input("Introduzca opción: ")
    if op == "A":
        engine.setProperty('voice',voices[0].id)
        break
    elif op == "B":
        engine.setProperty('voice',voices[1].id)
        break
    print("Intrpduzca \'A\' o \'B\' según su opción")

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

