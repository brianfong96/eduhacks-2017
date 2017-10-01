# eduhacks 2017
# Education/Sim/Tinder
# Player class

class player:
    def __init__(self, data):
        # ALL TEXTFILE READ WRITE WILL BE REPLACED WITH QUERIES TO DATABASE
        # check if there is saved data in saved text file
        try :
            self.file = open(data, 'r')
            self.reading_file = True
            self.data = []
            self.loading_data = False

            while self.reading_file:
                self.temp = self.file.readline()[:-1]
                if self.temp == "END":
                    self.reading_file = False
                else:
                    self.data.append(self.temp)

            print(self.data)

            self.loading_data = True
            while self.loading_data:
                


        # if not create new account and write to text file
        except:
            self.name = input("Please enter your name: ")
            # Mastery (Skill level of certain areas like math, science, etc.)
            self.mastery = {}   # Dictionary mapping skills to level
            # Currency (used to buy add on's)
            self.points = 0     # Used to access other players notes, and more
            # Note Bank (Player's notes for public or paid view)
            self.notes = []
            # Questions that player has
            self.question = []
            # Player answers to questions
            self.answers = []
            # Friends / Network
            self.friends = []
            

    
    def show_data(self):
        print("name = %s" %self.name)

    # save information to text/database

    # ask question

    # answer question

    # update notes



p = player("test.txt")