import tkinter as tk
from tkinter import ttk
import json

TITLE_FONT = ("Verdana", 20)

class DCM(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "CPU L8R")

        #container is the frame that we will populate depending on the page we need
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="True")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #tkraise brings the page we want that's in the back to the front
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome", font="TITLE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Log In",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(pady=10, padx=10)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font="TITLE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Log Out",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

app = DCM()
app.mainloop()
