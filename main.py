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

        self.LRL_button = ttk.Label(self, text="Lower Rate Limit")
        self.LRL_button.grid(row = 2, column = 1, pady=(10,0), padx=(10,10))
        
        self.LRL_slide = tk.Scale(self, from_ = 30, to = 175, orient = tk.HORIZONTAL)
        self.LRL_slide.grid(row = 3, column = 1, pady=(10,0), padx=(10,10))
        self.LRL_slide.set(60)
   
        
        self.URL_button = ttk.Label(self, text="Upper Rate Limit")
        self.URL_button.grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        
        self.URL_slide = tk.Scale(self, from_ = 50, to = 175, orient = tk.HORIZONTAL)
        self.URL_slide.grid(row = 3, column = 4, pady=(10,0), padx=(10,10))
        self.URL_slide.set(120)
        
        
        self.AA_button = ttk.Label(self, text="Atrial Amplitude")
        self.AA_button.grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        
        self.AA_slide = tk.Scale(self, from_ = 0.5, to = 7.0, orient = tk.HORIZONTAL)
        self.AA_slide.grid(row = 5, column = 1, pady=(10,0), padx=(10,10))
        self.AA_slide.set(3.5)
        
        
        self.APW_button = ttk.Label(self, text="Atrial Pulse Width")
        self.APW_button.grid(row = 4, column = 4, pady=(10,0), padx=(10,10))
        
        self.APW_slide = tk.Scale(self, from_ = 0.1, to = 1.9, orient = tk.HORIZONTAL)
        self.APW_slide.grid(row = 5, column = 4, pady=(10,0), padx=(10,10))
        self.APW_slide.set(0.4)
        
        
        self.AOO_Button = ttk.Button(self, text="Enter",
                            command= self.aooValues, cursor = "target")
        self.AOO_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))
        
        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))
        
    def aooValues(self): 
        usr = getRecent()
      
        update(usr, "aoo", "lower", self.LRL_slide.get())
        update(usr, "aoo", "upper", self.URL_slide.get())
        update(usr, "aoo", "AAmp",  self.AA_slide.get())
        update(usr, "aoo", "APW", self.APW_slide.get())

        return alert('Values added successfully') 
            
class VOO(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VOO", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 1, column = 3)

        self.LRL_button = ttk.Label(self, text="Lower Rate Limit")
        self.LRL_button.grid(row = 2, column = 1, pady=(10,0), padx=(10,10))
        
        self.LRL_slide = tk.Scale(self, from_ = 30, to = 175, orient = tk.HORIZONTAL)
        self.LRL_slide.grid(row = 3, column = 1, pady=(10,0), padx=(10,10))
        self.LRL_slide.set(60)
        
        
        self.URL_button = ttk.Label(self, text="Upper Rate Limit")
        self.URL_button.grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        
        self.URL_slide = tk.Scale(self, from_ = 50, to = 175, orient = tk.HORIZONTAL)
        self.URL_slide.grid(row = 3, column = 4, pady=(10,0), padx=(10,10))
        self.URL_slide.set(120)
        
        
        self.VA_button = ttk.Label(self, text="Ventricular Amplitude")
        self.VA_button.grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        
        self.VA_slide = tk.Scale(self, from_ = 0.5, to = 7.0, orient = tk.HORIZONTAL)
        self.VA_slide.grid(row = 5, column = 1, pady=(10,0), padx=(10,10))
        self.VA_slide.set(3.5)
        
        
        self.VPW_button = ttk.Label(self, text="Ventricular Pulse Width")
        self.VPW_button.grid(row = 4, column = 4, pady=(10,0), padx=(10,10))
        
        self.VPW_slide = tk.Scale(self, from_ = 0.1, to = 1.9, orient = tk.HORIZONTAL)
        self.VPW_slide.grid(row = 5, column = 4, pady=(10,0), padx=(10,10))
        self.VPW_slide.set(0.4)
        
        
        self.VOO_Button = ttk.Button(self, text="Enter",
                            command= self.vooValues, cursor = "target")
        self.VOO_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))
        
        
        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))
        
    def vooValues(self): 
        usr = getRecent()
      
        update(usr, "voo", "lower", self.LRL_slide.get())
        update(usr, "voo", "upper", self.URL_slide.get())
        update(usr, "voo", "VAmp",  self.VA_slide.get())
        update(usr, "voo", "VPW", self.VPW_slide.get())

        return alert('Values added successfully')  
        
        
class AAI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="AAI", font="TITLE_FONT")
        label.grid(pady=10, padx=10, row = 1, column = 2)

        self.LRL_label = ttk.Label(self, text="Lower Rate Limit")
        self.LRL_label.grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        
        self.LRL_slide = tk.Scale(self, from_ = 30, to = 175, orient = tk.HORIZONTAL)
        self.LRL_slide.grid(row = 3, column = 0, pady=(10,0), padx=(10,10))
        self.LRL_slide.set(60)

        
        self.URL_label = ttk.Label(self, text="Upper Rate Limit")
        self.URL_label.grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        
        self.URL_slide = tk.Scale(self, from_ = 50, to = 175, orient = tk.HORIZONTAL)
        self.URL_slide.grid(row = 3, column = 2, pady=(10,0), padx=(10,10))
        self.URL_slide.set(120)
        
        
        self.AA_label = ttk.Label(self, text="Atrial Amplitude")
        self.AA_label.grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        
        self.AA_slide = tk.Scale(self, from_ = 0.5, to = 7.0, orient = tk.HORIZONTAL)
        self.AA_slide.grid(row = 3, column = 4, pady=(10,0), padx=(10,10))
        self.AA_slide.set(3.5)
        
        
        self.APW_label = ttk.Label(self, text="Atrial Pulse Width")
        self.APW_label.grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        
        self.APW_slide = tk.Scale(self, from_ = 0.1, to = 1.9, orient = tk.HORIZONTAL)
        self.APW_slide.grid(row = 5, column = 1, pady=(10,0), padx=(10,10))
        self.APW_slide.set(0.4)
        
        
        self.ARP_label = ttk.Label(self, text="ARP")
        self.ARP_label.grid(row = 4, column = 3, pady=(10,0), padx=(10,10))
        
        self.ARP_slide = tk.Scale(self, from_ = 150, to = 500, orient = tk.HORIZONTAL)
        self.ARP_slide.grid(row = 5, column = 3, pady=(10,0), padx=(10,10))
        self.ARP_slide.set(320)
        
        
        self.AAI_Button = ttk.Button(self, text="Enter",
                            command= self.aaiValues, cursor = "target")
        self.AAI_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))
        
        
        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))
        
    def aaiValues(self): 
        usr = getRecent()
      
        update(usr, "aai", "lower", self.LRL_slide.get())
        update(usr, "aai", "upper", self.URL_slide.get())
        update(usr, "aai", "AAmp",  self.AA_slide.get())
        update(usr, "aai", "APW", self.APW_slide.get())
        update(usr, "aai", "ARP", self.ARP_slide.get())

        return alert('Values added successfully')  

                
class VVI(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="VVI", font="TITLE_FONT")
        label.grid(row = 1, column = 2, pady=10, padx=10)

        self.LRL_label = tk.Label(self, text="Lower Rate Limit")
        self.LRL_label.grid(row = 2, column = 0, pady=(10,0), padx=(10,10))
        
        self.LRL_slide = tk.Scale(self, from_ = 30, to = 175, orient = tk.HORIZONTAL)
        self.LRL_slide.grid(row = 3, column = 0, pady=(0,0), padx=(10,10))
        self.LRL_slide.set(60)

    
        self.URL_label = ttk.Label(self, text="Upper Rate Limit")
        self.URL_label.grid(row = 2, column = 2, pady=(10,0), padx=(10,10))
        
        self.URL_slide = tk.Scale(self, from_ = 50, to = 175, orient = tk.HORIZONTAL)
        self.URL_slide.grid(row = 3, column = 2, pady=(0,0), padx=(10,10))
        self.URL_slide.set(120)
        
        
        self.VA_label = ttk.Label(self, text="Ventricular Amplitude")
        self.VA_label.grid(row = 2, column = 4, pady=(10,0), padx=(10,10))
        
        self.VA_slide = tk.Scale(self, from_ = 0.5, to = 7.0, orient = tk.HORIZONTAL)
        self.VA_slide.grid(row = 3, column = 4, pady=(0,0), padx=(10,10))
        self.VA_slide.set(3.5)
        
        
        self.VPW_label = ttk.Label(self, text="Ventricular Pulse Width")
        self.VPW_label.grid(row = 4, column = 1, pady=(10,0), padx=(10,10))
        
        self.VPW_slide = tk.Scale(self, from_ = 0.1, to = 1.9, orient = tk.HORIZONTAL)
        self.VPW_slide.grid(row = 5, column =1, pady=(0,0), padx=(10,10))
        self.VPW_slide.set(0.4)
        
        
        self.VRP_label = ttk.Label(self, text="VRP")
        self.VRP_label.grid(row = 4, column = 3, pady=(10,0), padx=(10,10))
        
        self.VRP_slide = tk.Scale(self, from_ = 150, to = 500, orient = tk.HORIZONTAL)
        self.VRP_slide.grid(row = 5, column = 3, pady=(0,0), padx=(10,10))
        self.VRP_slide.set(320)
        
        
        self.VVI_Button = ttk.Button(self, text="Enter",
                            command= self.vviValues, cursor = "target")
        self.VVI_Button.grid(row = 20, column = 4, pady=(20,20), padx=(10,10))
        
        
        BACK_button = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        BACK_button.grid(row = 20, column = 0,  pady=(20,20), padx=(10,10))
        
    def vviValues(self): 
        usr = getRecent()
      
        update(usr, "vvi", "lower", self.LRL_slide.get())
        update(usr, "vvi", "upper", self.URL_slide.get())
        update(usr, "vvi", "VAmp",  self.VA_slide.get())
        update(usr, "vvi", "VPW", self.VPW_slide.get())
        update(usr, "vvi", "VRP", self.VRP_slide.get())

        return alert('Values added successfully')  
        
    
       
app = DCM()
app.mainloop()


