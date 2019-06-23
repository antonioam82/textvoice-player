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

print("\nENTER \'.\' TO FINISH THE PROGRAM AND SPACE(\' \') TO REPEAT THE LAST MESSAGE.\n")
texto=("")
prev_text=("")
speak=wc.Dispatch("Sapi.SpVoice")
while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=input("YOUR TEXT: ")
    if texto==(" "):
        if prev_text==(""):
            print("THERE'S NO PREVIOUS MESSAGE",chr(7))
        else:
            print("REPEATING THE LAST MESSAGE")
            speak.Speak(prev_text)
    else:
        speak.Speak(texto)
        prev_text=texto
