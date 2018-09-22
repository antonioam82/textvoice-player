import win32com.client as wc

print("REPRODUCCIÓN DE TEXTO MEDIANTE VOZ")
print("INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\' \') PARA REPETIR EL ÚLTIMO MENSAJE INTRODUCIDO/REPRODUCIDO")
texto=("")
prev_text=("")
speak=wc.Dispatch("Sapi.SpVoice")

def ns(op):
    while op!="n" and op!="s":
        op=input("Escriba solo \'n\' o \'s\' según su opción: ")
    return op

def re(t,regis,textos):
    if t!=".":
        if regis=="s":
            textos.append(t)
    return t
    
regis=ns(input("¿Desea registrar la conversación?: "))
textos=[]
if regis=="s":
    registro="conversacion.txt"
    fichero=open(registro,"w")
while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=re(input("TU TEXTO: "),regis,textos)
    if texto==(" "):
        if prev_text==(""):
            print("NO HAY MENSAJE ANTERIOR",chr(7))
        else:
            print("REPITIENDO MENSAJE")
            speak.Speak(prev_text)
    else:
        speak.Speak(texto)
        prev_text=texto
        
if regis=="s":
    for i in (textos):
        fichero.write(i+"\n")
    fichero.close()
    
