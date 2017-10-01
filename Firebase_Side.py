# eduhacks 2017
# Education/Sim/Tinder
# Player class

from firebase import firebase
firebase = firebase.FirebaseApplication('https://group-a1.firebaseio.com')
#url = 'https://group-a1.firebaseio.com/username'

# firebase.post('/account', {'username' : 'data', 'password' : 'Its data555', 'mastery' : 0, 'point' : 0, 'notes' : 0, 'questions' : 0,
#                                'answers' : 0, 'friends' : 0})


def get_key(username):
    tmp = '/' + username
    userData = firebase.get(tmp, None)
    if userData == None:
        return None
    key = next(iter(userData))
    return key

def get_info(username, key):
    tmp = '/'+username
    userData = firebase.get(tmp, None)
    if userData == None:
        return None
    key = get_key(username)
    info = userData[key]
    return info

def get_account(username, password):
    userData = get_info()   # dictionary of account info
    ret = None
    if userData != None:
        if password == userData["password"]:
            ret = []
            ret.append(userData["mastery"])
            ret.append(userData["points"])
            ret.append(userData["notes"])
            ret.append(userData["questions"])
            ret.append(userData["answer"])
            ret.append(userData["friends"])

    return ret

def delete_account(username):
    key = get_key(username)
    

    return

def write_account():
    return

def update_account():
    return



get_account("a", "b")