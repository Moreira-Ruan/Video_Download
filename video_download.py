import yt_dlp

# Lista de URLs de vídeos individuais
video_urls = [
    '',
    '',
    ''
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
