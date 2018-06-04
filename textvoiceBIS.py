import win32com.client as wc
print("REPRODUCCIÓN DE TEXTO MEDIANTE VOZ")
print("INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\' \') PARA REPETIR EL ÚLTIMO MENSAGE INTRODUCIDO/REPRODUCIDO")
texto=("")
prev_text=("")
voice=wc.Dispatch("Sapi.SpVoice")#Llamar al método Dispatch del módulo
while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=input("TU TEXTO: ")
    texto=texto.lower()
    if texto==(" "):
        if prev_text==(""):
            print("NO HAY MENSAGE ANTERIOR",chr(7))
        else:
            print("REPITIENDO MENSAGE")
            voice.Speak(prev_text)
    else:
        voice.Speak(texto)
        prev_text=texto
    
    
