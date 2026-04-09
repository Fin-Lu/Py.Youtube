# YouTube-Downloader | Python 3.12
# Autor: Fin
# Siehe "Erklärung" für Bedienungsanleitung und Voraussetzungen


import yt_dlp

def Download (url):
    ydl_opts = {
        'format': 'bestaudio/best',
        # '/Deine Pfade/%(title)s.%(ext)s'
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'keepvideo': False,
        'postprocessor_args': ['-vn'],

    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Die MP3 wird geladen! ")
    except Exception as e:
        print(f"Beim Download ist ist ein Fehler aufgetreten: {e}")

url = input("Bitte geben sie den Youtube Link ein (URL):  ")
Download(url)
