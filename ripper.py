# import
import tkinter as tk
from tkinter import ttk
import os

# functions
def download():
    # cmd = 'yt-dlp -o "'+name_string.get()+" "+filename_string.get()+'.mp4" --referer '+originalurl_string.get()+" "+rippurl_string.get()
    # print (os.system(cmd))
    cmd = 'yt-dlp -o "'+name_string.get()+""+filename_string.get()+'.mp4" --referer https://www.sex.com/ '+rippurl_string.get()
    print (os.system(cmd))

# MAIN CODE
# window setup
ripper = tk.Tk()
ripper.title('someProg Setup Wizzard')
ripper.geometry('800x400')

# title
title_lable = ttk.Label(
    master = ripper,
    text='I will get it for you...',
    font='Calibri 24 bold')
title_lable.pack()

# inputs
boxwidth = 100

input_frame = ttk.Frame(master=ripper)
    # everything that is put in entry will be stored in entryInt because of textvariable=...
name_label = ttk.Label(master=input_frame, text='Name, Names:')
name_string = tk.StringVar()
name = ttk.Entry(
    master=input_frame,
    width=boxwidth,
    textvariable=name_string)
filename_label = ttk.Label(master=input_frame, text='Filename:')
filename_string = tk.StringVar()
filename = ttk.Entry(
    master=input_frame,
    width=boxwidth,
    textvariable=filename_string)
# originalurl_label = ttk.Label(master=input_frame, text='Original URL:')
# originalurl_string = tk.StringVar()
# originalurl = ttk.Entry(master=input_frame, textvariable=originalurl_string)
rippurl_label = ttk.Label(master=input_frame, text='Ripp URL')
rippurl_string = tk.StringVar()
rippurl = ttk.Entry(
    master=input_frame,
    width=boxwidth,
    textvariable=rippurl_string)

button = ttk.Button(
    master=input_frame,
    text='Start Download',
    command=download)

name_label.pack()
name.pack()
filename_label.pack()
filename.pack()
# originalurl_label.pack()
# originalurl.pack()
rippurl_label.pack()
rippurl.pack()
button.pack(pady=20)
input_frame.pack()

# run
ripper.mainloop()