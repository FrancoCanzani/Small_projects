import pytube
from pytube import YouTube

video_url = input("""Bienvenido al descargador de YouTube de Franco Canzani
Inserte el URL del video, presione enter y aguarde mientras se descarga: """)
carpeta = input('Inserte la ruta a la carpeta donde desea que se descargue el video: ')
print('Iniciando descarga en maxima resolucion...')


for a in video_url:    
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        print('Descargado -> ' + youtube.title)
        video.download(carpeta)
    
    except:
        print(f'El url ({video_url}) o la direccion a la carpeta ({carpeta}) no es valido, intentelo nuevamente.')
