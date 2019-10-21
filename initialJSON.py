#Script used to create and initialize the users JSON file
import json

users = {
    "count":0
}
with open('users.json', 'w') as outfile:
    json.dump(users, outfile)
