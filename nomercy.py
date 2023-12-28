# No Mercy
# Cooperates on the first moves, once the opponent defect once, defect forever!
class noMercy :
    def __init__(self, hajar = False):
        self.hajar = False
        self.name = "No Mercy"
    
    def go(self, opponent):
        if opponent != 0 :
            if self.hajar == False :

                if opponent == 2 :
                    self.hajar = True
                    return 2 #Defect
                else :
                    return 1 #Cooperate

            else :
                return 2 #Defect
        else :
             return 1 #Cooperate