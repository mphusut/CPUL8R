#Funtions to adjust inputted values

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
