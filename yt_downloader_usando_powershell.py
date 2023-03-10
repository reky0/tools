import os

try:
    import pytube
except:
    os.system("python -m pip install pytube")

try: 
    import easygui as eg
except:
    os.system("python -m pip install easygui")
    import easygui as eg


video = input("Que video quieres descargar:  ")
ruta = eg.diropenbox("Selecciona una carpeta")

if "youtube" in video:
    os.system("pytube \"" + video + "\" -t \"" + ruta + "\"")