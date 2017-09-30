# eduhacks 2017
# Education/Sim/Tinder
# Player class

class player:
    def __init__(self, data):        
        # check if there is saved data in saved text file
        try :
            self.data = open(data, 'r')
            self.name = self.data[0]
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
        
    
