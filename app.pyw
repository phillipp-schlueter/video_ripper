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

        self.progress_var = tk.IntVar()
        self._build_gui()
        self._add_filename_with_format()


    def _build_gui(self):
        tk.Label(self.root, text="Video Ripper", font=("Arial", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(10, 20)
        )

        self.entry_name = self._add_entry("Name:", 1)
        self.entry_filename = self._add_entry("Filename:", 2)
        self.input_url = self._add_entry("URL:", 3)

        path_frame = tk.Frame(self.root)
        path_frame.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ttk.Button(path_frame, text="Save Path", command=self.select_path, width=12).grid(row=0, column=0, padx=10)
        self.folder_label = tk.Label(path_frame, text="Folderpath:")
        self.folder_label.grid(row=0, column=1, sticky="w", padx=15)

        self.action_frame = tk.Frame(self.root)
        self.action_frame.grid(row=5, column=0, padx=5, pady=10, sticky="w")

        ttk.Button(self.action_frame, text="Start Download", command=self.download).grid(row=0, column=0, padx=10)
        self.status_label = tk.Label(self.action_frame, text="")
        self.status_label.grid(row=0, column=1, padx=10)

        self.progress = ttk.Progressbar(self.action_frame, length=200, mode="determinate", variable=self.progress_var)
        self.progress.grid(row=0, column=2, padx=10)
        self.progress.grid_remove()

        self.percent_label = tk.Label(self.action_frame, text="")
        self.percent_label.grid(row=0, column=3, padx=5)

    def _add_filename_with_format(self):
        frame = tk.Frame(self.root)
        frame.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Label(frame, text="Filename:", width=12).grid(row=0, column=0, padx=10, sticky="w")
        self.entry_filename = ttk.Entry(frame, width=83)
        self.entry_filename.grid(row=0, column=1, padx=10)

        self.format_var = tk.StringVar()
        self.format_dropdown = ttk.Combobox(frame, textvariable=self.format_var, values=[".mp4", ".webm", ".mov", ".mkv"], width=10)
        self.format_dropdown.set(".mp4")
        self.format_dropdown.grid(row=0, column=2, padx=10)

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
        self.progress.grid_remove()
        self.percent_label.config(text="")
        self.status_label.after(3000, lambda: self.status_label.config(text=""))


    def update_progress(self, progress_dict):
        if progress_dict.get("status") == "downloading":
            total_bytes = progress_dict.get("total_bytes") or progress_dict.get("total_bytes_estimate")
            downloaded_bytes = progress_dict.get("downloaded_bytes", 0)
            if total_bytes:
                percent = (downloaded_bytes / total_bytes) * 100
                self.progress["value"] = percent
                self.root.update_idletasks()
        elif progress_dict.get("status") == "finished":
            self.progress["value"] = 100

    def download(self):
        if not self.folder_path:
            self.show_message("Please select a save path first.", "red")
            return

        self.progress_var.set(0)
        self.progress.grid()
        self.percent_label.config(text="0%")
        self.status_label.config(text="Starte Download...", foreground="black")
        self.root.update_idletasks()

        def update_progress(percent):
            self.progress_var.set(percent)
            self.percent_label.config(text=f"{percent}%")
            self.root.update_idletasks()

        try:
            print("Download wird gestartet mit Parametern:")
            print("Name:", self.entry_name.get())
            print("Filename:", self.entry_filename.get())
            print("URL:", self.input_url.get())
            print("Pfad:", self.folder_path)
            print("Format:", self.format_var.get())

            download_video(
                self.entry_name.get(),
                self.entry_filename.get(),
                self.input_url.get(),
                self.folder_path,
                self.format_var.get().lstrip("."),
                progress_callback=update_progress
            )
            self.show_message("Download erfolgreich!", "green")
        except Exception as e:
            print("Fehler beim Download:", e)
            self.show_message(f"Fehler: {e}", "red")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoRipperApp(root)
    root.mainloop()
