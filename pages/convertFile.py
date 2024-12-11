import tkinter
from youtube_download import youtube_download
import tkinter as tk
from tkinter import ttk
from ..converter import converter
from grapher import grapher
from startpage import startPage
from page2 import page2 
from ..main import frm 

class convertFile(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        def convert():
            file = entry.get()
            converter(file)
            label.configure(text="""conversion successful,
             look in folder for new file""")
            label.grid(column=2,row=0)

        entry = ttk.Entry(frm,text="Convert file")
        entry.grid(column=0, row=0)
        button = ttk.Button(frm,command=convert,text="filepath/filename")
        button.grid(column=1, row=0)
        label = ttk.Label(frm,text="")
        button3= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(startPage))
        button3.grid(column=0, row=3)
        button3 = ttk.Button(self, text="youtube download",
                             command=lambda: controller.show_frame(youtube_download))
        button3.grid(column=1, row=3)
        button3 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(page2))
        button3.grid(column=2, row=3)
        button4 = ttk.Button(self, text="graphing files",
                             command=lambda: controller.show_frame(grapher))
        button4.grid(column=0, row=3)

        label.grid_forget() 