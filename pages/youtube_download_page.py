
import tkinter as tk
from tkinter import ttk
from grapher import grapher
from startpage import startPage
from ..analyizer import VideoToText as vt
from convertFile import convertFile
from page2 import page2 
from ..main import frm


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
                vt(path_variable, link_var, filename)
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
        download_video.grid()
        button1  = ttk.Button(self, text="page 2",     
                              command=lambda: controller.show_frame(page2))
        button1.grid(column = 0, row = 0)
        button3 = ttk.Button(self, text="start page",
                             command=lambda: controller.show_frame(startPage))
        button3.grid(column=0, row=3)
        button4 = ttk.Button(self, text="gr",
                             command=lambda: controller.show_frame(grapher))
        button4.grid(column=0, row=3)
        button5 = ttk.Button(self, text="gr",
                             command=lambda: controller.show_frame(convertFile))
        button5.grid(column=0, row=4)