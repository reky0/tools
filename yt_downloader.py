import os

try:
    from pytube import YouTubeexcept:
except:
    os.system("python -m pip install pytube")
    from pytube import YouTube


chars = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890-'
chars = list(chars)
link_file = # ruta (recomendada absoluta) del archivo .txt que contiene los enlaces a descargar (uno por linea)
destino = # carpeta de destino (ruta absoluta recomendada)

with open(link_file) as file:
    for line in file:
        yt = YouTube(line)
        title = yt.title
        for char in title:
            if char in chars:
                if char.isupper() == True:
                    title = title.replace(char, char.lower())
            elif char == 'á' or char == 'Á':
                title = title.replace(char, 'a')
            elif char == 'é' or char == 'É':
                title = title.replace(char, 'e')
            elif char == 'í' or char == 'Í':
                title = title.replace(char, 'i')
            elif char == 'ó' or char == 'Ó':
                title = title.replace(char, 'o')
            elif char == 'ú' or char == 'Ú':
                title = title.replace(char, 'u')
            elif char == ' ':
                title = title.replace(char, '-')
            else:
                title = title.replace(char, '')

        if title[0] == '-':
            title = list(title)
            title[0] = ''
            
        title = ''.join(title)


        for i in range(0,4):
            if '--' in title:
                title = title.replace('--', '-')

            if '---' in title:
                title = title.replace('---', '-')

        title = title + '.mp4'

        try:
            yt.streams.get_highest_resolution().download(output_path=destino, filename=title)
        except:
            print('error al descargar ' + title)

    
    file.close()
