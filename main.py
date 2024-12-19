from pages.youtube_download import youtube_download
import tkinter as tk
from tkinter import ttk
from pages.grapher import grapher
from pages.startpage import startPage
from pages.convertFile import convertFile
from pages.page2 import page2 
from pages.youtube_download import youtube_download 

#vars
#tkinter set up

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (youtube_download, startPage, page2,convertFile, grapher):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(startPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
root = tkinterApp
root.title("Youtube Downloader and analyser")
frm = ttk.Frame(root, padding=10)
frm.grid()

root.geometry("400x400")
root.mainloop()
