import random

# Acak
# Randomly choose to cooperate or defect
class acak :
    def __init__(self):
        self.name = "Acak"

    def go(self, opponent):
        return random.choice([1,2])


# Good Guy
# Always Cooperates
class goodGuy :
    def __init__(self):
        self.name = "Good Guy"

    def go(self, opponent):
        return 1 #Cooperate   


# Bad Guy
# Always defects
class badGuy :
    def __init__(self):
        self.name = "Bad Guy"

    def go(self, opponent):
        return 2 #Cooperate

# Copy Cat
# Copy opponent prvious act
class copyCat :  
    def __init__(self):
        self.name = "Copy Cat"

    def go(self, opponent):
        if opponent != 0 :
            return opponent
        else :
             return 1 #Cooperate