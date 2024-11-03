# the yt-dlp.exe must be placed in the same folder as this script
import os
import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter.filedialog import askdirectory

# Globale Variable für den Ordnerpfad
folderpath = ""

def save(): 
    global folderpath
    folderpath = askdirectory()
    if folderpath:
        folder_label.config(text='Folderpath: ' + folderpath)

def show_message(message, color):
    status_label.config(text=message, foreground=color)
    status_label.after(3000, lambda: status_label.config(text=""))  # Clear after 3 seconds

def download():
    if not folderpath:
        show_message("Please select a path to save your file at first.", "red")
        return

    name = entry_name.get().strip() or "%(uploader)s"
    filename = entry_filename.get().strip() or "%(title)s"
    url = input_url.get()

    # Format the output file path
    output_template = os.path.join(folderpath, f"{name} {filename}.mp4")

    # Run yt-dlp to get the best format available
    cmd = [
        "yt-dlp", "-f", "bv*+ba/b",  # Get best video and audio, fallback to best single format
        "--merge-output-format", "mp4",  # Force output to mp4
        "-o", output_template,
        url
    ]

    # Run the download command and check the result
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Check for errors in the output
    if result.returncode == 0:
        show_message("Download successful!", "green")
    else:
        show_message("Download failed: " + result.stderr, "red")

root = tk.Tk()
root.title("Video Ripper")

tk.Label(root, text="Video Ripper", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 20))

label_width = 12
frames = [tk.Frame(root) for _ in range(6)]  # Anzahl der Frames auf 6 erhöhen

for i, frame in enumerate(frames):
    frame.grid(row=i + 1, column=0, padx=5, pady=5, sticky="w")

tk.Label(frames[0], text="Name:", width=label_width).grid(row=0, column=0, padx=10, sticky="w")
entry_name = ttk.Entry(frames[0], width=100)
entry_name.grid(row=0, column=1, padx=10)

tk.Label(frames[1], text="Filename:", width=label_width).grid(row=0, column=0, padx=10, sticky="w")
entry_filename = ttk.Entry(frames[1], width=83)
entry_filename.grid(row=0, column=1, padx=10)
file_format = ttk.Combobox(frames[1], values=['.mp4', '.mov'], width=10)
file_format.set('.mp4')
file_format.grid(row=0, column=2, padx=10)

button_save = ttk.Button(frames[2], text='Save Path', command=save, width=label_width)
button_save.grid(row=0, column=0, padx=10)
folder_label = tk.Label(frames[2], text="Folderpath:")
folder_label.grid(row=0, column=1, sticky="w", padx=15)

tk.Label(frames[3], text="URL:", width=label_width).grid(row=0, column=0, padx=10, sticky="w")
input_url = ttk.Entry(frames[3], width=100)
input_url.grid(row=0, column=1, padx=10)
input_url.insert(0, "https://www.reddit.com/r/NFSHeat/comments/1ghwaud/why_do_people_do_this/")

# Zeitrahmen (Start- und Endzeit)
tk.Label(frames[4], text="Zeit (hh:mm:ss)", width=label_width, foreground="grey").grid(row=0, column=0, padx=10, sticky="w")

start_hour_entry = ttk.Entry(frames[4], width=3, state="disabled")
start_hour_entry.grid(row=0, column=1, padx=(10, 0))
tk.Label(frames[4], text=":", foreground="grey", width=3).grid(row=0, column=2)
start_minute_entry = ttk.Entry(frames[4], width=3, state="disabled")
start_minute_entry.grid(row=0, column=3)
tk.Label(frames[4], text=":", foreground="grey", width=3).grid(row=0, column=4)
start_second_entry = ttk.Entry(frames[4], width=3, state="disabled")
start_second_entry.grid(row=0, column=5, padx=(0, 10))

tk.Label(frames[4], text="-", foreground="grey", width=3).grid(row=0, column=6)

end_hour_entry = ttk.Entry(frames[4], width=3, state="disabled")
end_hour_entry.grid(row=0, column=7, padx=(10, 0))
tk.Label(frames[4], text=":", foreground="grey", width=3).grid(row=0, column=8)
end_minute_entry = ttk.Entry(frames[4], width=3, state="disabled")
end_minute_entry.grid(row=0, column=9)
tk.Label(frames[4], text=":", foreground="grey", width=3).grid(row=0, column=10)
end_second_entry = ttk.Entry(frames[4], width=3, state="disabled")
end_second_entry.grid(row=0, column=11, padx=(0, 10))

# Button und Statuslabel in derselben Zeile
tk.Label(frames[5], width=label_width).grid(row=0, column=0, padx=10)
download_button = ttk.Button(frames[5], text='Start Download', command=download)
download_button.grid(row=0, column=1, padx=10, pady=10)

status_label = tk.Label(frames[5], text="")
status_label.grid(row=0, column=2, padx=10)  # Neben dem Download-Button platzieren

root.mainloop()
