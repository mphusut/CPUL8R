#Main
import tkinter as tk
from tkinter import ttk
import json
from tkinter import messagebox
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
#         self.minsize(400, 400)

        for F in (StartPage, RegisterPage, PageOne, AOO, VOO, AAI, VVI):
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
            recent(self.username.get())
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
        label = ttk.Label(self, text="CPUL8R", font="TITLE_FONT").pack()
        label = ttk.Label(self, text= "WELCOME " + getRecent(), font="TITLE_FONT")
        label.pack(pady=10, padx=10)



        AOO_button = ttk.Button(self, text="AOO",
                            command=lambda: controller.show_frame(AOO))
        AOO_button.pack(pady=5, padx=5)

        VOO_button = ttk.Button(self, text="VOO",
                            command=lambda: controller.show_frame(VOO))
        VOO_button.pack(pady=5, padx=5)

        AAI_button = ttk.Button(self, text="AAI",
                            command=lambda: controller.show_frame(AAI))
        AAI_button.pack(pady=5, padx=5)

        VVI_button = ttk.Button(self, text="VVI",
                            command=lambda: controller.show_frame(VVI))
        VVI_button.pack(pady=5, padx=5)


        LOGOUT_button = ttk.Button(self, text="Log Out",
                            command=lambda: controller.show_frame(StartPage))
        LOGOUT_button.pack(pady=25, padx=25)


class AOO(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AOO", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 1, column = 3)

        self.LRL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 2, column=1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.LRL_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.URL_Entry).grid(row = 3, column = 4, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.AA_Entry).grid(row = 5, column = 1, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.APW_Entry).grid(row = 5, column = 4, pady=(10,0), padx=(10,10))


        self.AOO_Button = ttk.Button(self, text="Enter",
                            command= self.aooValues, cursor = "target")
        self.AOO_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))

        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aooValues(self):
        usr = getRecent()

        update(usr, "aoo", "lower", setLRL(self.LRL_Entry.get()))
        update(usr, "aoo", "upper", setURL(self.URL_Entry.get()))
        update(usr, "aoo", "AAmp",  setAmp(self.AA_Entry.get()))
        update(usr, "aoo", "APW", setPW(self.APW_Entry.get()))

        return alert('Values added successfully:\n\n' +
        'lower: ' + str(setLRL(self.LRL_Entry.get())) + '\n'+
        'upper: ' + str(setURL(self.URL_Entry.get())) + '\n'+
        'AAmp: ' + str(setAmp(self.AA_Entry.get())) + '\n'+
        'APW: ' + str(setPW(self.APW_Entry.get())))

class VOO(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VOO", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 1, column = 3)

        self.LRL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 2, column=1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.LRL_Entry).grid(row = 3, column = 1, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.URL_Entry).grid(row = 3, column = 4, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.VA_Entry).grid(row = 5, column = 1, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.VPW_Entry).grid(row = 5, column = 4, pady=(10,0), padx=(10,10))

        self.VOO_Button = ttk.Button(self, text="Enter",
                            command= self.vooValues, cursor = "target")
        self.VOO_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def vooValues(self):
        usr = getRecent()

        update(usr, "voo", "lower", setLRL(self.LRL_Entry.get()))
        update(usr, "voo", "upper", setURL(self.URL_Entry.get()))
        update(usr, "voo", "VAmp",  setAmp(self.VA_Entry.get()))
        update(usr, "voo", "VPW", setPW(self.VPW_Entry.get()))

        return alert('Values added successfully:\n\n' +
        'lower: ' + str(setLRL(self.LRL_Entry.get())) + '\n'+
        'upper: ' + str(setURL(self.URL_Entry.get())) + '\n'+
        'VAmp: ' + str(setAmp(self.VA_Entry.get())) + '\n'+
        'VPW: ' + str(setPW(self.VPW_Entry.get())))


class AAI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AAI", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 1, column = 2)

        self.LRL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.LRL_Entry).grid(row = 3, column = 0, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.URL_Entry).grid(row = 3, column = 2, pady=(10,0), padx=(10,10))

        self.AA_Entry = tk.DoubleVar()
        ttk.Label(self, text="Atrial Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.AA_Entry).grid(row = 3, column = 4, pady=(10,0), padx=(10,10))

        self.APW_Entry = tk.DoubleVar()
        ttk.Label(self, text="Atrial Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.APW_Entry).grid(row = 5, column = 1, pady=(10,0), padx=(10,10))

        self.ARP_Entry = tk.DoubleVar()
        ttk.Label(self, text="Atrial Refractory Period\n(150-500)").grid(row = 4, column = 3, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.ARP_Entry).grid(row = 5, column = 3, pady=(10,0), padx=(10,10))

        self.AAI_Button = ttk.Button(self, text="Enter",
                            command= self.aaiValues, cursor = "target")
        self.AAI_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def aaiValues(self):
        usr = getRecent()

        update(usr, "aai", "lower", setLRL(self.LRL_Entry.get()))
        update(usr, "aai", "upper", setURL(self.URL_Entry.get()))
        update(usr, "aai", "AAmp",  setAmp(self.AA_Entry.get()))
        update(usr, "aai", "APW", setPW(self.APW_Entry.get()))
        update(usr, "aai", "ARP", setRP(self.ARP_Entry.get()))

        return alert('Values added successfully:\n\n' +
        'lower: ' + str(setLRL(self.LRL_Entry.get())) + '\n'+
        'upper: ' + str(setURL(self.URL_Entry.get())) + '\n'+
        'AAmp: ' + str(setAmp(self.AA_Entry.get())) + '\n'+
        'APW: ' + str(setPW(self.APW_Entry.get())) + '\n'+
        'ARP: ' + str(setRP(self.ARP_Entry.get())))


class VVI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VVI", font="TITLE_FONT")
        label.grid(row = 1, column = 2, pady=10, padx=10)

        self.LRL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Lower Rate Limit\n(30-175)").grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.LRL_Entry).grid(row = 3, column = 0, pady=(10,0), padx=(10,10))

        self.URL_Entry = tk.DoubleVar()
        ttk.Label(self, text="Upper Rate Limit\n(50-175)").grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.URL_Entry).grid(row = 3, column = 2, pady=(10,0), padx=(10,10))

        self.VA_Entry = tk.DoubleVar()
        ttk.Label(self, text="Ventricular Amplitude\n(0, 0.5-3.2, 3.5-7)").grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.VA_Entry).grid(row = 3, column = 4, pady=(10,0), padx=(10,10))

        self.VPW_Entry = tk.DoubleVar()
        ttk.Label(self, text="Ventricular Pulse Width\n(0.05, 0.1-1.9)").grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.VPW_Entry).grid(row = 5, column = 1, pady=(10,0), padx=(10,10))

        self.VRP_Entry = tk.DoubleVar()
        ttk.Label(self, text="Ventricular Refractory Period\n(150-500)").grid(row = 4, column = 3, pady=(10,0), padx=(10,10))
        ttk.Entry(self, textvariable=self.VRP_Entry).grid(row = 5, column = 3, pady=(10,0), padx=(10,10))

        self.VVI_Button = ttk.Button(self, text="Enter",
                            command= self.vviValues, cursor = "target")
        self.VVI_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))


        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))

    def vviValues(self):
        usr = getRecent()

        update(usr, "vvi", "lower", setLRL(self.LRL_Entry.get()))
        update(usr, "vvi", "upper", setURL(self.URL_Entry.get()))
        update(usr, "vvi", "VAmp",  setAmp(self.VA_Entry.get()))
        update(usr, "vvi", "VPW", setPW(self.VPW_Entry.get()))
        update(usr, "vvi", "VRP", setRP(self.VRP_Entry.get()))

        return alert('Values added successfully:\n\n' +
        'lower: ' + str(setLRL(self.LRL_Entry.get())) + '\n'+
        'upper: ' + str(setURL(self.URL_Entry.get())) + '\n'+
        'VAmp: ' + str(setAmp(self.VA_Entry.get())) + '\n'+
        'VPW: ' + str(setPW(self.VPW_Entry.get())) + '\n'+
        'VRP: ' + str(setRP(self.VRP_Entry.get())))


app = DCM()
app.mainloop()
