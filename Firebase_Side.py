# eduhacks 2017
# Education/Sim/Tinder
# Player class

from firebase import firebase
firebase = firebase.FirebaseApplication('https://group-a1.firebaseio.com')


def get_key(username):
    userData = firebase.get(username, None)
    if userData == None:
        return None
    key = next(iter(userData))
    return key

def get_info(username):
    userData = firebase.get(username, None)
    if userData == None:
        return None
    key = get_key(username)
    info = userData[key]
    return info

def get_account(username, password):
    userData = get_info(username)   # dictionary of account info
    ret = None
    if userData != None:
        if password == userData["password"]:
            ret = []
            ret.append(userData["mastery"])
            ret.append(userData["point"])
            ret.append(userData["notes"])
            ret.append(userData["questions"])
            ret.append(userData["answers"])
            ret.append(userData["friends"])

    return ret

def delete_account(username):
    firebase.delete(username, None)
    return

def write_account(username,password,mastery, points, notes, questions, answers, friends):
    firebase.post(username, {'password': password, 'mastery': mastery, 'points': points,
                             'notes': notes, 'questions': 0, 'answers' : answers, 'friends' : friends})
    return

def update_account():
    return


username = "account"
username = "/" + username
password = "a"
account = get_account(username, password)
if account != None:
    delete_account(username)
    print("Successful Delete")
else:
    print("Account does not exist")