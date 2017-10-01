# eduhacks 2017
# Education/Sim/Tinder
# Player class
import tmp as tmp


class Player:
    # constructor class check if database has info
    def __init__(self):
        # ALL TEXTFILE READ WRITE WILL BE REPLACED WITH QUERIES TO DATABASE
        # check if there is saved data in saved text file
        self.name = input("Please enter your name: ")
        self.password = input("Please enter your password: ")
        self.on = True
        
        self.data = tmp.get_account(self.name, self.password)
            # self.data = 

        # if not create new account and write to text file
        if self.data == None:
            # Mastery (Skill level of certain areas like math, science, etc.)
            self.mastery = {}   # Dictionary mapping skills to level
            # Currency (used to buy add on's)
            self.points = 0     # Used to access other players notes, and more
            # Note Bank (Player's notes for public or paid view)
            self.notes = []
            # Questions that player has
            self.questions = []
            # Player answers to questions
            self.answers = []
            # Friends / Network
            self.friends = []

        else:
            self.mastery = self.data[0] # dictionary format {skill_name: skill_points}
            self.points = self.data[1]  # currency
            self.notes = self.data[2]   # note bank (probably just name of files)
            self.questions = self.data[3]   # list of questions
            self.answers = self.data[4]     # list of answers
            self.friends = self.data[5]     # list of friend user_names
         

    # check if player is active
    def get_status(self):
        return self.on

    # TMake player inactive
    def turn_off(self):
        self.on = False
    
    # Display User profile
    def show_data(self):
        print("Username:\n%s" %self.name)
        print("Points:\n%d" %self.points)
        print("Question:")
        print(self.questions)

    # save information to text/database
    def save_account(self):
        save(self.name, self.password, self.mastery, self.points, self.notes, self.questions, self.answers, self.friends)

    # ask question
    def ask_question(self):
        getting_input = True
        tags = []
        userin = input("Enter a question that you want to ask: ")
        while getting_input:
            tag = input("Enter a tag for your question('end' to finish)")
            if tag.lower() == 'end':
                getting_input =False
            else:
                tags.append(tag)

        question = [tags, userin]
        self.questions.append(question)
        self.points += 1


    # answer question
    def answer_question(self):
        userin = input("Enter a topic that you would like to answer:\n")
        file = open("question.txt", "r")
        tag = file.readline()
        tag=tag.rstrip()
        #use key t 
        #also need to check if question has already been answered by user before
        if userin == tag:
            print(file.readlines())
        else:
            print("No question available on the selected topic.")
        file.close
    # get answer
        getting_input = True
        userin = input("Please enter your answer: ")
        file = open("answer.txt", "w")
        file.write(userin)
        file.close

    #update database

    #Keep answering questions
        action=input("Would you like to answer another question? (y/n)")
        if action=='Y'or action=='y':
            p.answer_question()

    # update notes



p = Player()
while p.get_status():
    action = input("""
What do you want to do? Enter:
1) See your profile
2) Ask a question
3) Answer a question
4) Quit
>> """)
    if action == '1':
        p.show_data()
    elif action == '2':
        p.ask_question()
    elif action == '3':
        p.answer_question()
    elif action == '4':
        p.turn_off()
    else :
        print("That is not a valid option")