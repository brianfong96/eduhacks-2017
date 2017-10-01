# eduhacks 2017
# Education/Sim/Tinder
# Player class
import Firebase_Side

class player:
    def __init__(self):
        # ALL TEXTFILE READ WRITE WILL BE REPLACED WITH QUERIES TO DATABASE
        # check if there is saved data in saved text file
        self.name = input("Please enter your name: ")
        self.password = input("Please enter your password: ")
        
        self.data = get_account(self.name, self.password)
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
            

    
    def show_data(self):
        print("Username:\t%s" %self.name)
        print("Points:\t%d" %self.points)

    # save information to text/database
    def save_account(self):
        save(self.name, self.password, self.mastery, self.points, self.notes, self.questions, self.answers, self.friends)

    # ask question
    def ask_question(self):
        userin = input("Enter a question that you want to ask: ")
        self.questions.append(userin)
        self.points += 1
        self.save_account()

    # answer question
    def answer_question(self):
        userin = input()
    # update notes



p = player()
p.show_Data