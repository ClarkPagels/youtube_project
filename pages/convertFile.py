import tkinter
from pages.youtube_download import youtube_download

from youtube_download import youtube as yt
from analyizer import VideoToText as vt
import tkinter as tk
from tkinter import ttk
import tokenizer
from converter import converter
import matplotlib as mpl 
import seaborn as sb
import tensorflow as tf
from plots.zipflaw import zipf
from plots.top_10_words import barChart
from pages.grapher import grapher
from pages.startpage import startPage
from pages.convertFile import convertFile
from pages.page2 import page2 
from pages.youtube_download import youtube_download 

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

        label.grid_forget() 