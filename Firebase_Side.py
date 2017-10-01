# eduhacks 2017
# Education/Sim/Tinder
# Player class

from firebase import firebase
firebase = firebase.FirebaseApplication('https://group-a1.firebaseio.com')

#firebase.post('/user', {'username' : 'Its data','password' : 'Its data'})


print (userData)
print (type (userData))


def get_account(name, password):
	userData = firebase.get(name, None)
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