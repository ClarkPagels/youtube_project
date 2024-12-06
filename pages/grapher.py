class grapher(tk.frame): 
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        file1 = ttk.Entry(frm,text="file you want")
        file1.grid(column=0, row=0)
        file2 = ttk.Entry(frm,text = "second file")
        file2.grid(column=0, row = 1)
        button = ttk.Button(frm,command=convert,text="filepath/filename")
        button.grid(column=1, row=0)
        label = ttk.Label(frm,text="")
        button2= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(startPage))
        button2.grid(column=0, row=3)
        button3 = ttk.Button(self, text="youtube download",
                             command=lambda: controller.show_frame(youtube_download))
        button3.grid(column=1, row=3)
        button4 = ttk.Button(self, text="convert file",
                             command=lambda: controller.show_frame(page2))
        button4.grid(column=2, row=3)