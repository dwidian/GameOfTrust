# Tit For Tat 
# Tit For Tat is similar to the philosophy of “an eye for an eye”. The punishment matches the crime. If someone defects against you, then immediate defect against them. If they start cooperating again, then you start cooperating again too. It’s the incarnation of strict fairness.
class TitforTat :
    def __init__(self, hajar = False):
        self.hajar = False
        self.name = "Tit for Tat"
    
    def go(self, opponent):
        if opponent != 0 :
            if self.hajar == False :
                if opponent == 2 :
                    self.hajar = True
                    return opponent
                else :
                    return 1 #Cooperate
            else :
                 return opponent
        else :
             return 1 #Cooperate