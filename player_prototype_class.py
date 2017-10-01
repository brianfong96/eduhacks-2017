# eduhacks 2017
# Education/Sim/Tinder
# Player class
# import Account_FBside as fb
import tmp as fb
# import QA_FBside as qa
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
                self.start.hideSubWindow("Main Menu")
            elif button == "Ask Q":
                self.ask_question()
                self.start.hideSubWindow("Main Menu")
            elif button == "Answer Q":
                print("ANSWER QUESTION BUTTON PRESSED")
                self.answer_question()
                self.start.hideSubWindow("Main Menu")
            elif button == "Quit":
                self.turn_off
                self.start.hideSubWindow("Main Menu")


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
        def press(button):
            self.start.hideSubWindow("Profile")
            self.start.showSubWindow("Main Menu")
        self.start.startSubWindow("Profile")
        self.start.addLabel("Profile", "Your profile details:")
        self.start.setFont(20)
        self.start.addLabel("p1","Username:\n%s" %self.name)
        self.start.addLabel("p2","Points:\n%s" %self.points)
        self.start.addLabel("p3", "Question:\n%s" %self.questions)
        self.start.addLabel("p4", "Answer:\n%s" %self.answers)
        self.start.addButton("Return", press)
        self.start.showSubWindow("Profile")
        
    # save information to text/database
    def save_account(self):
        print("SAVING ACOUNT")
        tmp_data = [self.mastery, self.points, self.notes, self.questions, self.answers, self.friends]
        fb.update_account(self.name, self.password, tmp_data)

    # ask question
    def ask_question(self):
        def press(button):
                if button == "Back":
                    self.start.hideSubWindow("Ask Q")
                    self.start.showSubWindow("Main Menu")
                elif button=="Enter":
                    self.cur_question = self.start.getEntry("Enter a question that you want to ask:")
                    print(self.cur_question)
                    self.start.hideSubWindow("Ask Q")
                    self.start.showSubWindow("Main Menu")

        print("ASKING QUESTION")
        getting_input = True
        self.start.startSubWindow("Ask Q")
        # get input from user
        self.start.addLabelEntry("Enter a question that you want to ask:")
        self.start.addLabelEntry("Tags, separate with //:")
        self.start.addButton("Back", press)
        self.start.addButton("Enter", press)
        self.start.showSubWindow("Ask Q")
        
        
        # REading into file 
        # question = "QUESTION//"
        # userin = input("Enter a question that you want to ask: ")
        # question += userin 
        # question += "//TAGS"
        # while getting_input:
        #     tag = input("Enter a tag for your question('end' to finish)")
        #     if tag.lower() == 'end':
        #         getting_input =False
        #     else:
        #         question = question + "//" + tag

        # self.questions = question


        self.points = str(int(self.points) + 1)

    # DOn't know what this does, commenting it o ut for now
    # def print_question(self):
    #     def press(button):
    #         #choose the question
    #         print("send help")
    #     self.start.startSubWindow("Display")
    #     file = open("question.txt", "r")
    #     line = file.readline()
    #     line=line.rstrip()
    #     words = line.split("//") 
    #     self.start.addLabel("")
    #     for word in words:
    #         if word == userin:
    #             self.start.addLabel(words[0])
    #     file.close  
    #     self.start.stopSubWindow()
    #     self.start.showSubWindow("Display")

    # answer question
    def answer_question(self):
        def press(button):
            if button == "search":
                print("PRESSING SEARCH BUTTON")
                self.start.showSubWindow("Question to Answer")
                self.start.hideSubWindow("Answer")
                #browse question
            elif button == "Answer":
                self.start.hideSubWindow("Question to Answer")
                self.start.showSubWindow("Main Menu")
            elif button == "Next":
                self.start.hideSubWindow("Answer")
                self.start.showSubWindow("Question to Answer")
            elif button == "Menu":
                self.start.stopSubWindow()
                self.start.showSubWindow("Main Menu")
            

        print("ANSWERING QUESTION")
        self.start.startSubWindow("Answer")
        self.start.addLabelEntry("Enter a question that you want to answer:")
        self.start.addButton("search",press)
        self.start.stopSubWindow()
       
        self.start.startSubWindow("Question to Answer")
        self.start.addLabelEntry("What is life?")
        self.start.addButton("Answer",press)
        self.start.addButton("Next",press) 
        self.start.addButton("Menu", press)   
        self.start.stopSubWindow()

      
        print("MAKING SUBWINDOW ANSWER")
        self.start.showSubWindow("Answer")


    #     file = open("question.txt", "r")
    #     line = file.readline()
    #     # use var = string.split("//")  will return a list split by the "//"
    #     line=line.rstrip()
    #     words = line.split("//")    # ["WHAT IS LIFE", "phil"]
    #     #use key t 
    #     #also need to check if question has already been answered by user before
    #     #how to search if user answered already 
    #     for word in words:
    #         if word == self.question:
    #             self.start.addLabel("Your question has been asked before: %s" %words[0])
    #     self.answer = self.start.addLabelEntry("Please enter your answer: ")        
    #     answer=userin+"//"+self.name
    #    # else:
    #         #print("No question available on the selected topic.")
    #     file.close
    # # get answer
    #     getting_input = True
    #     userin = input("Please enter your answer: ")
    #     #file = open("answer.txt", "w")
    #     #file.write(userin)
    #     #file.close
    #     #
    #     answer=userin+"//"+self.name
        # Add answer to user answers in STRING FORMAT
        
    #update database

    #Keep answering questions
        # action=input("Would you like to answer another question? (y/n)")
        # if action=='Y'or action=='y':
        #     p.answer_question()

    # update notes


if __name__ == "__main__":
    # def press(btn):
    #     print(btn)

    
    p = Player()
#     while p.get_status():
#         action = input("""
# What do you want to do? Enter:
# 1) See your profile
# 2) Ask a question
# 3) Answer a question
# 4) Quit
# >> """)
        
#         if action == '1':
#             p.show_data()
#         elif action == '2':
#             p.ask_question()
#         elif action == '3':
#             p.answer_question()
#         elif action == '4':
#             p.turn_off()
#         else :
#             print("That is not a valid option")

#     