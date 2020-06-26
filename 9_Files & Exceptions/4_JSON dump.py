import json

username = input('enter name : ')

filename = 'username.json'

with open(filename , 'w') as f_obj:
    json.dump(username, f_obj)
    print("we'll remember when you come back")
