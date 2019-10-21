import json
from tkinter import *

def checkCountUsers():
    with open('users.json') as json_file:
        data = json.load(json_file)
        if data["count"] >= 10:
            return False
        else:
            return True

def register(username, password):
    if checkCountUsers() == True and checkUsername(username)== False:
        with open('users.json') as json_file:
            data = json.load(json_file)

            count = data["count"]
            count +=1
            data["count"] = count
            data.update({username:password})

        with open('users.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    else:
        return False

def checkUsername(username):
    with open('users.json') as json_file:
        data = json.load(json_file)

    if username in data.keys():
        return True
    else:
        return False

def checkPassword(username, password):
    if checkUsername(username):
        with open('users.json') as json_file:
            data = json.load(json_file)
            if data[username] == password:
                return True
            else:
                return False
    else:
        return False

def deleteUser(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data.pop(username)
        count = data["count"]
        count -=1
        data["count"] = count

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

def alert(message):
    window = Toplevel()
    #window.minsize(300, 300)
    msg = Message(window, text=message)
    msg.pack()

    button = ttk.Button(window, text="Dismiss", command=window.destroy)
    button.pack(pady=3)
