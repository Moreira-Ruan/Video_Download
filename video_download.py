import yt_dlp

# Lista de URLs de vídeos individuais
video_urls = [
    'https://www.youtube.com/watch?v=pAEd1qEfCEw&list=PLB9D73ypDbAUpitzq2VOOvxGlPGdzBTMU&index=1',
    'https://www.youtube.com/watch?v=NtntbPpfqbc&list=PLB9D73ypDbAUpitzq2VOOvxGlPGdzBTMU&index=8',
    'https://www.youtube.com/watch?v=OGqf-zsZw6s&list=PLB9D73ypDbAUpitzq2VOOvxGlPGdzBTMU&index=4'
]

# Diretório de download
download_path = '/home/moreira/Documentos/Dev Web Full Stack/Video download/Downloads'

# Opções de download
ydl_opts = {
    'format': 'best',
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
}

# Baixar cada vídeo
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_urls)

print("Download completo!")
