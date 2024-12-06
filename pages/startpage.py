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

class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = ttk.Button(self, text="youtube_download",
                             command=lambda: controller.show_frame(youtube_download))
        button.grid(column=0, row=0)
        button1 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(converter))
        button1.grid(column=1, row=0)
        button2 = ttk.Button(self, text="text analysis",
                             command=lambda: controller.show_frame(page2))
        button2.grid(column=2, row=0)