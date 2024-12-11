import tkinter
from ..analyizer import VideoToText as vt
import tkinter as tk
from tkinter import ttk
from . import tokenizer
from ..converter import converter

from grapher import grapher
from convertFile import convertFile
from page2 import page2 
from youtube_download import youtube_download 
from ..main import frm
class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = ttk.Button(self, text="youtube_download",
                             command=lambda: controller.show_frame(youtube_download))
        button.grid(column=0, row=0)
        button1 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(converter))
        button1.grid(column=0, row=1)
        button2 = ttk.Button(self, text="text analysis",
                             command=lambda: controller.show_frame(page2))
        button2.grid(column=0, row=2)
        button3 = ttk.Button(self, text="graphing files",
                             command=lambda: controller.show_frame(grapher))
        button3.grid(column=0, row=3)