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
            ret.append(userData["points"])
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
                             'notes': notes, 'questions': questions, 'answers' : answers, 'friends' : friends})
    return

def update_account(username, password, userData):
    delete_account(username)
    write_account(username, password, userData[0], userData[1], userData[2], userData[3], userData[4],
                  userData[5])
    return

if __name__ == "__main__":
    username = "account"
    username = "/" + username
    password = "a"
    account = get_account(username, password)
    if account != None:
        delete_account(username)
        print("Successful Delete")
    else:
        print("Account does not exist")
        userIn = input("Do you want to make an account?(Y/N)")
        if userIn.upper() == 'Y':
            write_account(username, password, 10, 100, "my note", "question", "answ", "5")
            print ("echoing account")
            print(get_info(username))
        else:
            print("Closing App")