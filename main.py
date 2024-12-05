import tkinter

from youtube_download import youtube as yt
from analyizer import VideoToText as vt
import tkinter as tk
from tkinter import ttk
import tokenizer
from converter import converter
import matplotlib as mpl 
import seaborn as sb
import tensorflow as tf

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
        for F in (youtube_download, page2,convertFile):
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
class youtube_download(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
#tkinter functions
        def store_variable():
            global path_variable
            path_variable=entry.get()
            intro.configure(text=path_variable)

        def store_video():
            global link_var
            link_var= url_entry.get()

        def fileName():
            global filename
            filename= fileInput.get()
        def download_video():
            try:
                yt(path_variable, link_var, filename)
                Notification.grid(column=0,row=3)
            except:
                error.grid(column=1,row=3)




#tkinter interaction
        Notification = ttk.Label(frm, text="""Download successful,
        text file created""")
        Notification.grid_forget()

        error = ttk.Label(frm, text="Youtube error.Error")
        error.grid_forget()

        intro = ttk.Label(frm, text = """Here you will 
        be downloading a youtube video 
        of your choise and analysing it 
        how you will""")
        intro.grid(column=0, row=0,columnspan=2)


        location = ttk.TextBox(frm, text="""put in location of where 
        you want video to be downloaded to """)
        location.grid(column=1, row=1)

        entry = ttk.Entry(frm)
        entry.grid(column=2, row=1)

        youtube_video = ttk.Label(frm, text = """put in the url
        of the video you wish to download""")
        youtube_video.grid(column = 3, row = 1)

        url_entry = ttk.Entry(frm)
        url_entry.grid(column = 4, row = 1)



        set_destination = ttk.Button(frm, text = "Set destination",
                                 command=lambda: [store_variable(),store_video(),fileName()])
        set_destination.grid(column = 0, row = 2)

        Set = ttk.Label(frm, text="Put in name of the file you want video to be")
        Set.grid(column = 1, row = 2)

        fileInput = ttk.Entry(frm)
        fileInput.grid(column=2, row = 2)

        download_video = ttk.Button(frm,text = "download video",
                           command=download_video)
        download_video.grid(column = 3, row = 2)
        button2 = ttk.Button(self, text="analyizer ",
                         command=lambda: controller.show_frame(page2))
        button2.grid(column = 0, row = 0)
        button3 = ttk.Button(self, text="start page",
                             command=lambda: controller.show_frame(startPage))
        button3.grid(column=0, row=3)
        button4 = ttk.Button(self, text="youtube downloader",
                             command=lambda: controller.show_frame(convertFile))
        button4.grid(column=0, row=3)

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


root.mainloop()
