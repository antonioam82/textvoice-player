import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
text = ""

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

while text != ".":
    text = input("TEXT: ")
    engine.say(text)
    engine.runAndWait()
