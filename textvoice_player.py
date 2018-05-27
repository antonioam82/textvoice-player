import winspeech
print("TEXT_VOICE")
print("ENTER \'.\' TO FINISH THE PROGRAM AND SPACE (\' \') TO REPIT THE PREVIOUS MESSAGE")
texto=("")
prev_text=("")
while texto!=("."):
    texto=input("Your text: ")
    if texto==(" "):
        if prev_text==(""):
            print(chr(7),"THERE'S NOT A PREVIOUS MESSAGE")
        else:
            winspeech.say(prev_text)
    else:
        winspeech.say(texto)
        prev_text=texto
