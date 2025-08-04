import os
import imageio_ffmpeg
from yt_dlp import YoutubeDL

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

def download_video(name, filename, url, folder_path, file_format, progress_callback=None):
    name = name.strip() or "%(uploader)s"
    filename = filename.strip() or "%(title)s"
    url = url.strip()
    file_format = file_format.strip().lower()

    output_template = os.path.join(folder_path, f"{name} {filename}.{file_format}")

    def hook(d):
        if progress_callback and d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes:
                percent = int(downloaded_bytes / total_bytes * 100)
                progress_callback(percent)

    ydl_opts = {
        'format': 'bv*+ba/b',
        'merge_output_format': file_format,
        'outtmpl': output_template,
        'ffmpeg_location': ffmpeg_path,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [hook]
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

