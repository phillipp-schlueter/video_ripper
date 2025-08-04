import os
import imageio_ffmpeg
from yt_dlp import YoutubeDL

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

def download_video(name, filename, url, folder_path):
    name = name.strip() or "%(uploader)s"
    filename = filename.strip() or "%(title)s"
    url = url.strip()

    output_template = os.path.join(folder_path, f"{name} {filename}.mp4")

    ydl_opts = {
        'format': 'bv*+ba/b',
        'merge_output_format': 'mp4',
        'outtmpl': output_template,
        'ffmpeg_location': ffmpeg_path,
        'quiet': True,
        'no_warnings': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])