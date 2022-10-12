#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import os
import pyttsx3
import pickle
 
if not 'directorios' in os.listdir():
    fichero = open('directorios','wb')
    pickle.dump([],fichero)
    fichero.close()
 
lista_temas = []
direc = pickle.load(open('directorios','rb'))
nums = {'cero':0,'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5,'seis':6,'siete':7,'ocho':8,'nueve':9,
        'diez':10,'once':11,'doce':12,'trece':13,'catorce':14,'quince':15}
 
def async_playback(filename):
    data, fs = sf.read(filename)
    sd.play(data,fs)
    return data, fs
 
def cambia_microfono():
    sd.stop()###################################################################################
    num_micros = len(sr.Microphone.list_microphone_names())
    while True:
        print("\n****************************MICROFONOS DISPONIBLES****************************")
        for i in enumerate(sr.Microphone.list_microphone_names()):
            print(i)
        print("******************************************************************************\n")
        speaker("DIGA EN ALTO EL NÚMERO CORRESPONDIENTE AL MICRÓFONO DESEADO.",1)
        opcionn = listening()
        if opcionn == 'salir':
            speaker("PROCESO DE SELECCIÓN CANCELADO.",1)
            break
        else:
            try:
                if opcionn in nums:
                    opcion = nums[opcionn]
                else:
                    opcion = int(opcionn)
                if opcion >= 0 and opcion <= num_micros-1:
                    sd.default.device=opcion
                    print("\nINDICE MICRÓFONO: ",opcion)
                    speaker("nuevo microfono establecido correctamente",0)
                    break
                else:
                    speaker("INDICE FUERA DE RANGO",1)
            except Exception as e:
                print(str(e))
 
 
def listening():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        r.adjust_for_ambient_noise(source)
        r.energy_threshold=300#10050
 
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language='es-ES')
            print("TEXTO: ",text)
            return text
        except:
            print("Sin entrada")
            pass
 
def select_audio():
    while True:
        opcionn = listening()
        if opcionn == "lista":
            while True:
                print("\n********************LISTA DE AUDIOS********************")
                for elem,tema in enumerate(lista_temas):
                    print(elem,tema)
                print("*******************************************************\n")
                texto = "DIGA EN VOZ ALTA EL NÚMERO CORRESPONDIENTE AL AUDIO DESEADO."
                speaker(texto,1)
 
                opcionn = listening()
 
                if opcionn != "salir" and opcionn != "finalizar":
                    if opcionn == "comandos":
                        comandos()
                    else:
                        if opcionn in nums:
                            eleccion = nums[opcionn]
                        else:
                            eleccion = opcionn
 
                        print(type(eleccion))
                        try:
                            tema = int(eleccion)
                            assert tema in range(len(lista_temas))
                            audio_selec = lista_temas[tema]
                            print("AUDIO SELECCIONADO: {}".format(audio_selec))
                            async_playback(audio_selec)
                            break
                        except Exception as e:
                            print(str(e))
                            list_inn = False
                            speaker("NO SE PUDO PROCESAR LA SOLICITUD.",1)
                else:
                    if opcionn == "salir":
                        speaker("PROCESO DE SELECCIÓN CANCELADO.",1)
                    break
 
        if opcionn == 'para':
            list_inn = False
            sd.stop()
            print('STOPPED')
            speaker("audio interrumpido",0)
        if opcionn == 'finalizar':
            sd.stop()
            speaker("programa finalizado, hasta pronto",0)
            break
        if opcionn == 'cambia micrófono':
            cambia_microfono()
        if opcionn == 'comandos':
            comandos()
        if opcionn == 'colecciones':
            change_dir()
 
def speaker(content,v):
    engine.say(content)
    if v == 1:
        print(content)
    engine.runAndWait()
    engine.stop()
 
def validate_num(value):
    if value in nums:
        return nums[value]
    else:
        return value
 
def change_dir():
    global lista_temas
    sd.stop()
    while True:
        print("\n****************************COLECCIONES****************************")
        for elem,di in enumerate(direc):
            print(elem,di)
        print("*******************************************************************\n")
 
        speaker("DIGA EN VOZ ALTA EL NÚMERO CORRESPONDIENTE AL DIRECTORIO DESEADO.",1)
        opcionn = listening()
        if opcionn != 'salir':
            try:
                num = validate_num(opcionn)
                os.chdir(direc[int(num)])
                lista_temas = []
                collect()
                speaker("DIRECTORIO ESTABLECIDO CORRECTAMENTE.",1)
                print("\nCARPETA: ",os.getcwd())
                break
            except:
                speaker("NO SE PUDO PROCESAR LA SOLICITUD.",1)
        else:
            speaker("PROCESO DE SELECCIÓN CANCELADO.",1)
            break
 
def comandos():
    print("\n********************COMANDOS DE VOZ********************")
    print("'lista'-------------------------MUESTRA LISTA DE AUDIOS")
    print("'para'------------------FINALIZA REPRODUCCIÓN DEL AUDIO")
    print("'finalizar'------------------------FINALIZA EL PROGRAMA")
    print("'cambia micrófono'--------------------CAMBIAR MICROFONO")
    print("'comandos'----------------------MUESTRA COMANDOS DE VOZ")
    print("'colecciones'-----------------CAMBIAR CARPETA DE AUDIOS")
    print("'salir'-------------------CANCELAR PROCESO DE SELECCIÓN")
    print("********************************************************\n")
 
def collect():
    for i in glob.glob("*.wav"):
        lista_temas.append(i)
    if len(lista_temas) == 0:
        print("CARPETA VACÍA\n")
        speaker("la carpeta seleccionada no contiene archivos válidos",0)
        return False
    return True
 
def enter_dir(changed):
    new_dir = input("INTRODUZCA DIRECTORIO: ")
    if not new_dir in direc:
        if os.path.isdir(new_dir):
            direc.append(new_dir)
            pickle.dump(direc,open("directorios","wb"))
            os.chdir(new_dir)
            collect()
            speaker("DIRECTORIO ESTABLECIDO CORRECTAMENTE.",1)
            print("\nCARPETA: ",os.getcwd())
            changed=True
        else:
            speaker("EL DIRECTORIO NO EXISTE.",1)
    else:
        speaker("EL DIRECTORIO YA SE ENCUENTRA GUARDADO.",1)
    return changed
 
 
 
#sd.default.device=9 #CAMBIAR DISPOSITIVO DE "ENTRADA/SALIDA"
 
engine = pyttsx3.init()
engine.setProperty('rate',160)
 
while True:
    #comandos()
 
    print("\n****************************COLECCIONES****************************")
    for elem,di in enumerate(direc):
        if os.path.isdir(di):
            print(elem,di)
    print("*******************************************************************\n")
 
    if len(direc)>0:
        speaker('''DIGA EN VOZ ALTA EL NÚMERO CORRESPONDIENTE AL DIRECTORIO DESEADO,
'NUEVO' PARA AÑADIR UNO NUEVO O 'ELIMINAR' PARA BORRARLO''',1)
        opcionn = listening()
 
        if opcionn == 'nuevo':
            speaker("introduzca nuevo directorio",0)
            chang = enter_dir(changed=False)
            if chang == True:
                break
 
        elif opcionn == 'eliminar':
            speaker("DIGA EN VOZ ALTA EL NÚMERO CORRESPONDIENTE A LA COLECCIÓN A ELIMINAR.",1)
            num = listening()
            numero = validate_num(num)
            if str(numero).isdigit():
                try:
                    direc.remove(direc[int(numero)])
                    print(direc)
                    pickle.dump(direc,open("directorios","wb"))
                    speaker("COLECCIÓN ELIMINADA SATISFACTORIAMENTE.",1)
                except Exception as e:
                    print(str(e))
                    speaker("no se pudo realizar la acción",0)
            else:
                speaker("NO SE PUDO PROCESAR LA SOLICITUD.",1)
 
        else:
            numero = validate_num(opcionn)
            if str(numero).isdigit() and len(direc)>0:
                try:
                    new_dir = direc[int(numero)]
                    os.chdir(new_dir)
                    continue_ = collect()
                    if continue_:
                        speaker("DIRECTORIO ESTABLECIDO CORRECTAMENTE.",1)
                        print("\nCARPETA: ",os.getcwd())
                        break
                except Exception as e:
                    print(str(e))
                    speaker("NO SE PUDO PROCESAR LA SOLICITUD.",1)
    else:
        speaker("INTRODUZCA RUTA A LA COLECCIÓN.",1)
        chang = enter_dir(changed=False)
        if chang == True:
            break
 
comandos()
select_audio()
