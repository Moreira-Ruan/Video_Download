import yt_dlp
import os

# Lista de URLs de vídeos individuais
video_urls = [
    'https://www.youtube.com/watch?v=jyVezrgQ_uk&t=8s'
]

# Diretório de download
download_path = os.path.join(os.getcwd(), "Downloads")

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
