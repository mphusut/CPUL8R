import tkinter as tk
from tkinter import ttk
import json
from logins import *

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

        for F in (StartPage, RegisterPage, PageOne):
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
        ttk.Label(self, text="Welcome", font="TITLE_FONT").grid(row = 0, column=1, padx=30, pady=10)
        self.controller = controller
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        ttk.Label(self, text="Username").grid(row = 1, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.username).grid(row = 1, column=1, padx=(20,40), pady=2)
        ttk.Label(self, text="Password").grid(row = 2, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.password).grid(row = 2, column=1, padx=(20,40), pady=2)

        #ttk.Button(self, text="Log In", command=lambda: controller.show_frame(PageOne)).grid(row = 3, column=0, padx=10, pady=10)
        ttk.Button(self, text="Log In", command=self.login).grid(row = 1, column=2, padx=10, pady=5)
        ttk.Button(self, text="New User?", command=lambda: controller.show_frame(RegisterPage)).grid(row = 4, column=1,padx=10, pady=5)

    def login(self):
        if checkPassword(self.username.get(), self.password.get()):
            self.controller.show_frame(PageOne)
        else:
            return alert('Incorrect Username or Password!')

class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Register", font="TITLE_FONT").grid(row = 0, column=1, padx=30, pady=10)
        self.controller = controller
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        ttk.Label(self, text="Username").grid(row = 1, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.username).grid(row = 1, column=1, padx=(20,40), pady=2)
        ttk.Label(self, text="Password").grid(row = 2, column=0, padx=5, pady=2)
        ttk.Entry(self, textvariable=self.password).grid(row = 2, column=1, padx=(20,40), pady=2)

        #ttk.Button(self, text="Log In", command=lambda: controller.show_frame(PageOne)).grid(row = 3, column=0, padx=10, pady=10)
        ttk.Button(self, text="Register", command=self.adduser).grid(row = 3, column=1, padx=10, pady=5)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).grid(row = 4, column=1,padx=10, pady=5)

    def adduser(self):
        if checkCountUsers() == False:
            return alert('Too Many Users')
        elif register(self.username.get(), self.password.get()) == True:
            return alert('Registration Successful')
        else:
            return alert('User Already Exists')

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="CPUL8R", font="TITLE_FONT")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Log Out",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=10, padx=10)

app = DCM()
app.mainloop()
