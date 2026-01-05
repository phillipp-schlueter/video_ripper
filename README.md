# 🎥 Video Ripper GUI

A modern, lightweight desktop application to download videos from YouTube and other platforms easily. Built with `Python` and `tkinter`, it leverages the power of `yt-dlp` to ensure high-quality downloads without complex command-line usage.

## ✨ Features

- **🖥️ Simple GUI:** Clean interface built with `tkinter`. No command line needed.
- **⚡ High-Quality Downloads:** Uses `yt-dlp` to automatically merge the best video and audio streams (`bv*+ba`).
- **📦 FFmpeg Included:** Powered by `imageio-ffmpeg`, so you don't need to manually install or configure FFmpeg on your system.
- **📝 Custom Naming:** Define your own output names and filenames directly in the app.
- **📊 Real-time Progress:** Visual progress bar and percentage display to track your download status.
- **🎞️ Multiple Formats:**
  - Support for `.mp4`, `.webm`, `.mov`, `.mkv`.

## 🚀 Installation

1. **Clone the repository**
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Usage:**
    - Start the app
    - Enter a name and maybe a filename (otherwise original filename is choosen)
    - Enter an URL
    - Click "Save Path" to choose where the file should be saved.
    - Select your desired container format
    - Click "Start Download" and wait for the progress bar to finish.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

Distributed under the MIT License. See LICENSE.md for more information.
