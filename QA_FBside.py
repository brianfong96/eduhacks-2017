# eduhacks 2017
# Education/Sim/Tinder
# Player class

from appJar import gui
from firebase import firebase
firebase = firebase.FirebaseApplication('https://qhub-answerquestion.firebaseio.com')

def write_question(questionContent, questionId, userId, answerContent, answerId, mentorId):
    print("QA_FBside | write_question")

    if questionContent[-1] == '?':
        questionContent = questionContent[:-1]
        print("Deletting ? from %s" %questionContent)
    print("running question")

    firebase.post(questionContent, {'qContent' : questionContent, 'questionId' : questionId, 'userId': userId,
                                    'answerContent' : answerContent, 'answerId' : answerId, 'mentorId' : mentorId})
    print("finish writing")

def get_key(question):
    print("QA_FBside | get_key")

    if question[-1] == '?':
        question = question[:-1]
    questionData = firebase.get(question, None)
    if questionData == None:
        return None
    key = next(iter(questionData))
    return key

def get_info(question):
    print("QA_FBside | get_Info")
    if question[-1] == '?':
        question = question[:-1]
    questionData = firebase.get(question, None)
    if questionData == None:
        return None
    else:
        theKey = get_key(question)
        info = questionData[theKey]

    return info

def get_question(question):
    print("QA_FBside | get_question")

    if question[-1] == '?':
        question = question[:-1]
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

if __name__ == '__main__':
    q = "q3 is here?"
    qID = "0"
    uID = "12"
    ans = "None"
    answerId = "None"
    mentorId = "None"
    result = get_question(q)
    if result == None:
        print("question does not exist...writing question")
        write_question(q,qID,uID,ans,answerId,mentorId)
        if get_question(q) != None:
            print("WRITE WAS SUCCESSFUL!")
        else:
            print("try again in the next life")
    else:
        print("IT EXISTS")
        print(result)


