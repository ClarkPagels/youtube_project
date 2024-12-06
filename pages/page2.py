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


class page2(tk.frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def word_Counter():
            input = textBox.get(1.0,"end-1c")
            answer = tokenizer.wordCounter(input)
            number.configure(text=answer)
        def mostCommonWord():
            input = textBox1.get(1.0,"end-1c")
            answer = tokenizer.most_common_words(input)
            number1.configure(text=answer)
        def Sentiment():
            input = textBox2.get(1.0,"end-1c")
            answer = tokenizer.sentiment(input)
            number2.configure(text=answer)
        textBox = ttk.Text(frm, text="""file you want to read text from""")
        textBox.grid(column=0, row=0)
        button = ttk.Button(frm, text = "Sentiment", command=word_Counter)
        button.grid(column=1, row=0)
        number = ttk.Label(frm,text="")
        number.grid(column=2, row=0)

        textBox1 = ttk.Text(frm,text="find sentiment")
        textBox1.grid(column=0, row=1)
        button1 = ttk.Button(frm, text = "Sentiment", command=Sentiment)
        button1.grid(column=1, row=1)
        number1 = ttk.Label(frm,text="")
        number1.grid(column=2, row=0)

        textBox2 = ttk.Text(frm,text="find most common word")
        textBox2.grid(column=0, row=2)
        button2 = ttk.Button(frm, text = "Sentiment", command=mostCommonWord)
        button2.grid(column=1, row=2)
        number2 = ttk.Label(frm,text="")
        number2.grid(column=2, row=2)

        button3= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(startPage))
        button3.grid(column=0, row=3)
        button3 = ttk.Button(self, text="youtube download",
                             command=lambda: controller.show_frame(youtube_download))
        button3.grid(column=1, row=3)
        button3 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(convertFile))
        button3.grid(column=2, row=3)
        button4 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(grapher))
        