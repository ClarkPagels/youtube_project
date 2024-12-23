
import tkinter as tk
from tkinter import ttk
from ..plots.zipflaw import zipf
from ..plots.top_10_words import barChart
from startpage import startPage
from convertFile import convertFile
from page2 import page2 
from youtube_download_page import youtube_download as ydp
from ..main import frm

class grapher(tk.frame): 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        file1 = ttk.Entry(frm,text="file you want")
        file1.grid(column=0, row=0)
        file2 = ttk.Entry(frm,text = "second file if dessired")
        file2.grid(column=1, row = 0)
      
        zipfer = ttk.Button(self, text="zipf for file 1",
                          command = lambda: zipf(file1))
        zipfer.grid(column=0, row=2)
        barCharter = ttk.button(self, text="barchart words", 
                                command= lambda: barChart(file1))
        button2= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(startPage))
        button2.grid(column=0, row=3)
        button3 = ttk.Button(self, text="youtube download",
                             command=lambda: controller.show_frame(ydp))
        button3.grid(column=1, row=3)
        button4 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(page2))
        button4.grid(column=2, row=3)
        button= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(convertFile))
        button.grid(column=3, row=3)