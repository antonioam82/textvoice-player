import winspeech
print("TEXT_VOICE")
print("INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\' \') PARA REPETIR EL ÚLTIMO MENSAGE INTRODUCIDO/REPRODUCIDO")
texto=("")
prev_text=("")
while texto!=("."):
    texto=input("TU TEXTO EN INGLÉS: ")
    if texto==(" "):
        if prev_text==(""):
            print(chr(7),"NO HAY MENSAGE ANTERIOR")
        else:
            print("REPITIENDO MENSAGE")
            winspeech.say(prev_text)
    else:
        winspeech.say(texto)
        prev_text=texto
