import win32com.client as wc
print("REPRODUCCIÓN DE TEXTO MEDIANTE VOZ")
print("INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\' \') PARA REPETIR EL ÚLTIMO MENSAGE INTRODUCIDO/REPRODUCIDO")
texto=("")
prev_text=("")
speak=wc.Dispatch("Sapi.SpVoice")
while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=input("TU TEXTO: ")
    if texto==(" "):
        if prev_text==(""):
            print("NO HAY MENSAGE ANTERIOR",chr(7))
        else:
            print("REPITIENDO MENSAGE")
            speak.Speak(prev_text)
    else:
        speak.Speak(texto)
        prev_text=texto
