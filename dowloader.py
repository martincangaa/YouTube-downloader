# @carver 10042023

import pkg_resources
import subprocess

directorio = "" # Pega aqui el directorio en el que quieras que se descargue el video Ej(C:/Users/juancho/Desktop) PD: Recuerda usar "/" en vez de "\"

library = "pytube"
try:
    
    pkg_resources.get_distribution(library)
    print(f"{library} está ya instalado")
except pkg_resources.DistributionNotFound:
    
    print(f"{library} no esta instalado. Instalando {library}...")
    subprocess.check_call(["pip", "install", library])
    print(f"{library} se ha instalado yuhuu!!")

from pytube import YouTube

print("Que quieres hacer [1] descargar video / [2] descargar solo el audio:")

start  = int(input()) 
url = str(input("Pega el link de tu video: "))

def getStart():
    if(start == 1 or start == 2):
        return start
    else:
        print("No has introducido un valor valido")

def descargar_video():
    if(getStart() == 1):  
        yt = YouTube(url).streams.get_highest_resolution()
        try:
            yt.download(directorio)
        except:
            print("Error...")
    else:
        yt = YouTube(url).streams.get_audio_only()
        try:
            yt.download(directorio)
        except:
            print("Error descargando el video...")
    
descargar_video()