import yt_dlp
import os

# Lista de URLs individuais
music_urls = [
    'https://www.youtube.com/watch?v=lArnKBTe82I',
    'https://www.youtube.com/watch?v=CMIT4dB8pYw',
    'https://www.youtube.com/watch?v=igxnqo9hFpA',
    'https://www.youtube.com/watch?v=ryShwZcffIw'
]

# Diretório de download
download_path = os.path.join(os.getcwd(), "Downloads")

# Opções de download para áudio
ydl_opts = {
    'format': 'bestaudio/best',  # Baixar apenas o melhor áudio
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Nome do arquivo
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Formato de áudio desejado (MP3, pode mudar para 'wav' ou 'm4a')
        'preferredquality': '192',  # Qualidade do áudio (pode ajustar)
    }],
}

# Baixar apenas o áudio
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(music_urls)

print("Download de áudio completo!")
