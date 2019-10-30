import json
from tkinter import *

# Checks JSON object for User count to ensure that maximum of 10 users is maintained
def checkCountUsers():
    with open('users.json') as json_file:
        data = json.load(json_file)
        if data["count"] >= 10:
            return False
        else:
            return True

#Registers NeW uSeRs into the JSON file
def register(username, password):
    #Checks user count to ensure that more than 10 users are no created
    #Checks username to ensure that it doesn't already exist
    if checkCountUsers() == True and checkUsername(username)== False:
        with open('users.json') as json_file:
            data = json.load(json_file)
            count = data["count"]
            count +=1
            data["count"] = count
            #initialize user information
            data.update({username:{
            "password":password,
            "aoo":{"lower":60,"upper":120,"AAmp":3.5, "APW":0.4},
            "voo":{"lower":60,"upper":120,"VAmp":3.5, "VPW":0.4},
            "aai":{"lower":60,"upper":120,"AAmp":3.5, "APW":0.4, "ARP":250},
             "vvi":{"lower":60,"upper":120,"VAmp":3.5, "VPW":0.4, "VRP":320}}})
        #dumps info into JSON file
        with open('users.json', 'w') as json_file:
            json.dump(data, json_file)

        #return true if registration was successful
        return True
    else:
        #return false if registration was unsuccessful
        return False

#Checks if username already exists (for register function)
def checkUsername(username):
    with open('users.json') as json_file:
        data = json.load(json_file)

    if username in data.keys():
        return True
    else:
        return False

#Validates if correct password was inputed
def checkPassword(username, password):
    if checkUsername(username):
        with open('users.json') as json_file:
            data = json.load(json_file)
        if data[username]["password"] == password:
            recent(username)
            return True
        else:
            return False
    else:
        return False

#Stores the most recent user login
def recent(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data["recent"] = username

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#Updates parameters for each mode (called in main.py to update values)
def update(username, mode, key, value):
    with open('users.json') as json_file:
        data = json.load(json_file)

        data[username][mode][key] = value

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#deletes user from JSON and updates count
def deleteUser(username):
    with open('users.json') as json_file:
        data = json.load(json_file)
        data.pop(username)
        count = data["count"]
        count -=1
        data["count"] = count

    with open('users.json', 'w') as json_file:
        json.dump(data, json_file)

#general purpose alert window to display confirmations and errors
def alert(message):
    window = Toplevel()
    #window.minsize(300, 300)
    msg = Message(window, text=message)
    msg.pack()

    button = ttk.Button(window, text="Dismiss", command=window.destroy)
    button.pack(pady=3)

#Retrieves the username of the user that is currently logged in
def getRecent():
    with open('users.json') as json_file:
        data = json.load(json_file)
        return data["recent"]

#Adjusts the input value of the Lower Rate Limit to match the range and increment requirements
def setLRL(value):
    if value <= 30:
        return 30
    elif value > 175:
        return 175
    elif value >30 and value <=50:
        return int((value // 5)*5)
    elif value >50 and value <=90:
        return int(round(value))
    elif value >90 and value <=175:
        return int((value // 5)*5)

#Adjusts the input value of the Upper Rate Limit to match the range and increment requirements
def setURL(value):
    if value <= 50:
        return 50
    elif value > 50 and value < 175:
        return int((value // 5)*5)
    else:
        return 175

#Adjusts the input value of the Atrial/Ventricular Amplitude to match the range and increment requirements
def setAmp(value):
    if value == 0:
        return 0
    elif value <= 0.5:
        return 0.5
    elif value > 0.5 and value < 3.2:
        return round(value,1)
    elif value >=3.2 and value <3.5:
        return 3.2
    elif value >=3.5 and value < 7:
        return 0.5 * round(value/0.5)
    else:
        return 7.0

#Adjusts the input value of the Atrial/Ventricular Pulse Width to match the range and increment requirements
def setPW(value):
    if value >= 0.1 and value <= 1.9:
        return round(value,1)
    else:
        return 0.05

#Adjusts the input value of the Atrial/Ventricular Refractory Period to match the range and increment requirements
def setRP(value):
    if value <= 150:
        return 150
    elif value > 150 and value < 500:
        return 10 * round(value/10)
    else:
         return 500