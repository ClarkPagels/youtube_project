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