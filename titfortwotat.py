# Tit for two Tat
# Cooperates on the first move, and defects only when the opponent defects two times in a row
class TitforTwoTat :
    def __init__(self, prevAct = 0):
        self.prevAct = 0
        self.name = "Tit for two Tat"
    
    def go(self, opponent):
        if opponent != 0 :
            if self.prevAct == 0 :
                self.prevAct = opponent
                return 1 #Cooperate
            else :
                if ((self.prevAct == 2) and (opponent == 2)) :
                    self.prevAct = opponent
                    return 2 #Defect
                else :
                    self.prevAct = opponent
                    return 1 #Cooperate
        else :
             return 1 #Cooperate