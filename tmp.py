
def get_account(name, password):

	if name == "test" and password == "test":
		ret = []
		
		# masery
		ret.append("Math:10, Science:20")
		# points
		ret.append("300")
		# notes
		ret.append("notes.txt")
		# questions
		ret.append("QUESTION//what is life//TAG//Philosophy")
		# answers
		ret.append("QUESTION//what is life//TAG//Philosophy//ANSWER//there is no answer")
		# friends
		ret.append(["1friend"])
	else:
		ret = None
	return ret

def get_question(tag):
	questions = [["biology"],"what is a dog"]
	return questions