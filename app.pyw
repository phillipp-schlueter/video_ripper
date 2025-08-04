import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from downloader import download_video

class VideoRipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Ripper")
        self.folder_path = ""
        self._build_gui()

    def _build_gui(self):
        tk.Label(self.root, text="Video Ripper", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 20))
        self.entry_name = self._add_entry("Name:", 1)
        self.entry_filename = self._add_entry("Filename:", 2)
        self.input_url = self._add_entry("URL:", 3)
        self.input_url.insert(0, "https://www.reddit.com/r/NFSHeat/comments/1ghwaud/why_do_people_do_this/")

        path_frame = tk.Frame(self.root)
        path_frame.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ttk.Button(path_frame, text="Save Path", command=self.select_path, width=12).grid(row=0, column=0, padx=10)
        self.folder_label = tk.Label(path_frame, text="Folderpath:")
        self.folder_label.grid(row=0, column=1, sticky="w", padx=15)

        action_frame = tk.Frame(self.root)
        action_frame.grid(row=5, column=0, padx=5, pady=10, sticky="w")
        ttk.Button(action_frame, text="Start Download", command=self.download).grid(row=0, column=0, padx=10)
        self.status_label = tk.Label(action_frame, text="")
        self.status_label.grid(row=0, column=1, padx=10)

    def _add_entry(self, label, row):
        frame = tk.Frame(self.root)
        frame.grid(row=row, column=0, padx=5, pady=5, sticky="w")
        tk.Label(frame, text=label, width=12).grid(row=0, column=0, padx=10, sticky="w")
        entry = ttk.Entry(frame, width=100)
        entry.grid(row=0, column=1, padx=10)
        return entry

    def select_path(self):
        path = askdirectory()
        if path:
            self.folder_path = path
            self.folder_label.config(text="Folderpath: " + path)

    def show_message(self, message, color):
        self.status_label.config(text=message, foreground=color)
        self.status_label.after(3000, lambda: self.status_label.config(text=""))

    def download(self):
        if not self.folder_path:
            self.show_message("Please select a save path first.", "red")
            return

        try:
            download_video(
                self.entry_name.get(),
                self.entry_filename.get(),
                self.input_url.get(),
                self.folder_path
            )
            self.show_message("Download erfolgreich!", "green")
        except Exception as e:
            self.show_message(f"Fehler: {e}", "red")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoRipperApp(root)
    root.mainloop()
