# eduhacks 2017
# Education/Sim/Tinder
# Player class

from firebase import firebase
firebase = firebase.FirebaseApplication('https://qhub-answerquestion.firebaseio.com')

firebase.post("adasd", {'questionId' : 566, 'user_id': 789})
# def write_question(questionContent, questionId, userId):
#     firebase.post(questionContent, {'questionId' : questionId, 'user_id': userId})

def write_answer(questionId, answerContent, answerNo, answerId, mentorId):
    firebase.post(questionId, {'answerContent' : answerContent, 'answerNo:' : answerNo, 'answerId' : answerId,
                               'mentorId' : mentorId})


# qContent = 'Why?'
# qId = '0'
# userId = '00'
# write_question(qContent, qId, userId)