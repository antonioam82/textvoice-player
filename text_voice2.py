#!/usr/bin/env python
# -*- coding: utf-8 -*-
import win32com.client as wc
from colorama import init, Fore, Back, Style

init()

print(Back.YELLOW+Fore.RED+Style.DIM+" _________                                                          ")
print(Back.YELLOW+Fore.RED+Style.DIM+"|___   ___|                                                         ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    | | _____        _____               ______  __  ______  _____  ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    | ||  ___|/\  /\|_   _|   /\      /\|  __  ||  ||  ____||  ___| ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    | || |    \ \/ /  | | ____\ \    / /| |  | ||  || |     | |     ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    | || >>>   \  /   | ||    |\ \  / / | |  | ||  || |     | >>>   ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    | || |___  /  \   | ||____| \ \/ /  | |__| ||  || |____ | |___  ")
print(Back.YELLOW+Fore.RED+Style.DIM+"    |_||_____|/_/\_\  |_|        \__/   |______||__||______||_____| ")
print(Back.YELLOW+Fore.RED+Style.DIM+"--------------------------------------------------------------------")
print(Back.YELLOW+Fore.RED+Style.DIM+"--------------------------------------------------------------------\n"+"\033[39m")

print(Back.BLUE+Fore.RESET+Style.DIM+"""INTRODUCE \'.\' PARA FINALIZAR EL PROGRAMA Y ESPACIO (\'\') PARA REPETIR
EL ÚLTIMO MENSAJE INTRODUCIDO/REPRODUCIDO.                          \n""")

texto=("")
prev_text=("")
speak=wc.Dispatch("Sapi.SpVoice")
print(Back.RESET+Fore.GREEN+"")

while texto!=("."): #MIENTRAS QUE "texto" SEA DISTINTO A "."
    texto=input("TU TEXTO: ")
    if texto==(" "):
        if prev_text==(""):
            print(Fore.RED+"NO HAY MENSAJE ANTERIOR",Fore.GREEN+chr(7))
        else:
            print(Fore.RED+"REPITIENDO MENSAJE",Fore.GREEN)
            speak.Speak(prev_text)
    else:
        speak.Speak(texto)
        prev_text=texto
