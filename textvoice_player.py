#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client as wc
print(" _________")
print("|___   ___|")
print("    | | _____        _____               ______  __  ______  _____  ")
print("    | ||  ___|/\  /\|_   _|   /\      /\|  __  ||  ||  ____||  ___| ")
print("    | || |    \ \/ /  | | ____\ \    / /| |  | ||  || |     | |     ")
print("    | || >>>   \  /   | ||    |\ \  / / | |  | ||  || |     | >>>   ")
print("    | || |___  /  \   | ||____| \ \/ /  | |__| ||  || |____ | |___  ")
print("    |_||_____|/_/\_\  |_|        \__/   |______||__||______||_____| ")
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
print("")
print("""INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\' \') PARA REPETIR
EL ÚLTIMO MENSAJE INTRODUCIDO/REPRODUCIDO.""")
print("")
texto=("")
prev_text=("")
speak=wc.Dispatch("Sapi.SpVoice")
while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=input("TU TEXTO: ")
    if texto==(" "):
        if prev_text==(""):
            print("NO HAY MENSAJE ANTERIOR",chr(7))
        else:
            print("REPITIENDO MENSAJE")
            speak.Speak(prev_text)
    else:
        speak.Speak(texto)
        prev_text=texto

