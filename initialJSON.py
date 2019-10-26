#Script used to create and initialize the users JSON file
import json

#initialize count to 0 and recent to blank
users = {
    "count":0,
    "recent":"",
}
with open('users.json', 'w') as outfile:
    json.dump(users, outfile)
