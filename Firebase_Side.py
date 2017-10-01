# eduhacks 2017
# Education/Sim/Tinder
# Player class

from firebase import firebase
firebase = firebase.FirebaseApplication('https://group-a1.firebaseio.com')
#url = 'https://group-a1.firebaseio.com/username'

# firebase.post('/account', {'password' : 'Its data', 'mastery' : 0, 'point' : 0, 'notes' : 0, 'questions' : 0,
#                               'answers' : 0, 'friends' : 0})


def get_account(username, password):
    userData = firebase.get('/account', None)

    key = next(iter(userData))
    sDictionary = userData[key]
    [sDictionary['password']]

    if userData != None:
        ret = []
        ret.append(userData["mastery"])
        ret.append(userData["points"])
        ret.append(userData["notes"])
        ret.append(userData["questions"])
        ret.append(userData["answer"])
        ret.append(userData["friends"])
    else:
        ret = None

    return ret