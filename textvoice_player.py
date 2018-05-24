import winspeech

texto=("")
while texto!=("."):
    texto=input("Your text: ")
    winspeech.say(texto)
