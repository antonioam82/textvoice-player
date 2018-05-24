import winspeech
print("TEXT_VOICE")
print("ENTER \'.\' TO FINISH THE PROGRAM")
texto=("")
while texto!=("."):
    texto=input("Your text: ")
    winspeech.say(texto)
    
