# eduhacks 2017
# Education/Sim/Tinder
# Player class

from appJar import gui
from firebase import firebase
firebase = firebase.FirebaseApplication('https://qhub-answerquestion.firebaseio.com')

def write_question(questionContent, questionId, userId, answerContent, answerId, mentorId):
    firebase.post(questionContent, {'qContent' : questionContent, 'questionId' : questionId, 'userId': userId,
                                    'answerContent' : answerContent, 'answerId' : answerId, 'mentorId' : mentorId})

def get_key(question):
    questionData = firebase.get(question, None)
    if questionData == None:
        return None
    key = next(iter(questionData))
    return key

def get_info(question):
    questionData = firebase.get(question, None)
    if questionData == None:
        return None
    else:
        theKey = get_key(question)
        info = questionData[theKey]

    return info

def get_question(question):
    questionData = get_info(question)   # dictionary of account info
    ret = None
    if questionData != None:
        ret = []
        ret.append(questionData["qContent"])
        ret.append(questionData["questionId"])
        ret.append(questionData["userId"])
        ret.append(questionData["answerContent"])
        ret.append(questionData["answerId"])
        ret.append(questionData["mentorId"])

    return ret


#write_question("q2 is here", 1, 11, "No way", 111, 1235)
result = get_question("q2 is here")
print(result)