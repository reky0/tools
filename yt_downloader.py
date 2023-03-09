import pytube

url = input("Que video quieres descargar:  ")
path = "C:/Users/rault/Desktop/yt_downloader"

yt = pytube.YouTube(url)

print("Titulo..........: " + str(yt.title))
print("Duracion (seg)..: " + str(yt.length))

audiost = yt.streams.filter(only_audio=True, file_extension='mp4')

print("\n-----------AUDIO---------")
for st in audiost:
    print(str(st).replace("<Stream: itag=\"", "ITAG: ").replace("\" mime_type=\"", "  FORMATO: ").replace("\" abr=\"", "  RESOLUCION: ").replace("\"", ""))

videost = yt.streams.filter(only_video=True, file_extension='mp4')

print("\n\n-----------VIDEO---------")
for st in videost:
    print(str(st).replace("<Stream: itag=\"", "ITAG: ").replace("\" mime_type=\"", "  FORMATO: ").replace("\" res=\"", "  RESOLUCION: ").replace("\" fps=\"24fps\"", "").replace("\"", ""))

descarga = input("\nElige el video a descargar mediante su \"itag\":  ")

if descarga.isalnum() == True:
    st = yt.streams.get_by_itag(descarga)
    st.download(path)
else: 
    print("Ese \"itag\" no es valido")
