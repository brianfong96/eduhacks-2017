# eduhacks 2017
# Education/Sim/Tinder
# Player class
import Account_FBside as fb
import random
from datetime import datetime
import QA_FBside as qa
from appJar import gui

# import tmp as fb # use this when database is down

class Player:
    # constructor class check if database has info
    def __init__(self):
        print("IN  INIT")
        # ALL TEXTFILE READ WRITE WILL BE REPLACED WITH QUERIES TO DATABASE
        # check if there is saved data in saved text file

        self.start=gui()
        self.start.addLabel("title", "Welcome to Question Hub")
        self.start.addLabel("l1", "")
        self.start.setLabelBg("title", "blue")
        self.start.addLabelEntry("Username")
        self.start.addLabelSecretEntry("Password")
        self.on = True
        def press(button):
            if button == "Cancel":
                self.start.stop()
            else:

                self.name = self.start.getEntry("Username")
                self.password = self.start.getEntry("Password")
                print("User:", self.name, "Pass:", self.password)
                print("GETTING ACCOUNT")
                self.data = fb.get_account(self.name, self.password)


                # if not create new account and write to text file
                if self.data == None:
                    print("THIS ACCOUNT DOES NOT EXIST...MAKING NEW")
                    # Mastery (Skill level of certain areas like math, science, etc.)
                    self.mastery = ""   # Dictionary mapping skills to level
                    # Currency (used to buy add on's)
                    self.points = "0"     # Used to access other players notes, and more
                    # Note Bank (Player's notes for public or paid view)
                    self.notes = ""
                    # Questions that player has
                    self.questions = ""
                    # Player answers to questions
                    self.answers = ""
                    # Friends / Network
                    self.friends = ""
                    self.save_account() # save newly made account
                else:
                    print("LOADING EXISTING ACCOUNT")
                    self.mastery = self.data[0] # dictionary format {skill_name: skill_points}
                    self.points = self.data[1]  # currency
                    self.notes = self.data[2]   # note bank (probably just name of files)
                    self.questions = self.data[3]   # list of questions
                    self.answers = self.data[4]     # list of answers
                    self.friends = self.data[5]     # list of friend user_names

                self.main_menu()

        self.start.addButtons(["Submit", "Cancel"], press)
        #self.name = input("Please enter your name: ")
        #self.password = input("Please enter your password: ")

        # self.data =
        self.start.go()


    def main_menu(self):
        print("IN  MAIN MENU")
        def press(button):
            if button == "Profile":
                self.show_data()
            elif button == "Ask Q":
                self.ask_question("ask")
            elif button == "Answer Q":
                self.answer_question()
            elif button == "Quit":
                self.turn_off


        self.start.startSubWindow("Main Menu")
        self.start.addLabel("Menu", "Welcome to the Main Menu, select an option")
        self.start.addButtons(["Profile", "Ask Q", "Answer Q", "Quit"], press)
        self.start.stopSubWindow()
        self.start.showSubWindow("Main Menu")


    # check if player is active
    def get_status(self):
        print("IN GET STATUS")
        return self.on

    # TMake player inactive
    def turn_off(self):
        print("TURNING OFF")
        self.on = False

    # Display User profile
    def show_data(self):
        print("IN SHOW DATA")
        self.start.startSubWindow("Profile")
        self.start.addLabel("Profile", "Your profile details:")
        self.start.setFont(20)
        self.start.addLabel("Username:\n%s" %self.name)
        self.start.addLabel("Points:\n%s" %self.points)
        self.start.addLabel("Question:\n%s" %self.questions)
        self.start.addLabel("Answer:\n%s" %self.answers)
        self.start.stopSubWindow()
        self.start.showSubWindow("Main Menu")

    # save information to text/database
    def save_account(self):
        print("SAVING ACOUNT")
        tmp_data = [self.mastery, self.points, self.notes, self.questions, self.answers, self.friends]
        fb.update_account(self.name, self.password, tmp_data)

    def randomFunc(self):
        #random.seed(datetime.now())
        randomId = random.randint(1, 100)

        return str(randomId)

    # ask question
    def ask_question(self, prompt):
        print("ASKING QUESTION")
        getting_input = True
        userin = input("Enter a question that you want to %s: " %prompt)
        question = qa.get_question(userin)
        randomIdOne = self.randomFunc()
        randomIdTwo = self.randomFunc()

        if question == None:
            qa.write_question(userin, randomIdOne, randomIdTwo, "", (randomIdOne*2), (randomIdTwo*2))
        else:
            if question[3] == "":

                answerChoice = input("It has not been answered. Would you like to answer it? (y/n)")
                if answerChoice == 'y':
                    answer = input("Answer: ")
                    qa.write_question(userin, randomIdOne, randomIdTwo, answer, (randomIdOne*43), (randomIdTwo*52))
                else:
                    print("No worries")

            else:
                print(question[3])

        self.questions = question
        self.points = str(int(self.points) + 1)


    def answer_question(self):
        self.ask_question("answer")


if __name__ == "__main__":
    def press(btn):
        print(btn)

    
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

    