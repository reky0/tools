import getpass
import os

try:
    import pytube
except:
    os.system("python -m pip install pytube")
    import pytube

try: 
    import easygui as eg
except:
    os.system("python -m pip install easygui")
    import easygui as eg

path = eg.diropenbox("Selecciona una carpeta")

def elegirCancion():
    url = input("Que video quieres descargar:  ")

    yt = pytube.YouTube(url)

    return yt

def descargar(cancion):
    try:
        st = cancion.streams.get_highest_resolution()
        st.download(path)
    except:
        os.system('cls')
        input("HUBO UN ERROR, INTÉNTELO DE NUEVO")

cancion = elegirCancion()

descargar(cancion)