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
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    'merge_output_format': 'mp4'
}

# Baixar cada vídeo
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_urls)

print("Download completo!")
