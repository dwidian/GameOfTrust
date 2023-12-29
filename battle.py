def battle(round, contender1, contender2, VERBOSE = False) :

    P1 = contender1()    # Player 1
    P2 = contender2()    # Player 2

    P1_Score = 0        # Player 1 Score
    P2_Score = 0        # Player 2 Score

    for i in range(round):    # x rounds
        if i == 0 :
            P1_Act = P1.go(0)
            P2_Act = P2.go(0)
        else :
            P1_Act = P1.go(PrevP2_Act)
            P2_Act = P2.go(PrevP1_Act)

        PrevP1_Act = P1_Act
        PrevP2_Act = P2_Act

        # Log
        #print("P1 : {}, P2 : {}".format(P1_Act, P2_Act))

        if (P1_Act == 1) and (P2_Act == 1) :
            P1_Score = P1_Score + 3
            P2_Score = P2_Score + 3
        if (P1_Act == 2) and (P2_Act == 2) :
            P1_Score = P1_Score + 1
            P2_Score = P2_Score + 1
        if (P1_Act == 1) and (P2_Act == 2) :
            P2_Score = P2_Score + 5        
        if (P1_Act == 2) and (P2_Act == 1) :
            P1_Score = P1_Score + 5                  

    if VERBOSE :
        print("Final Score for {} is {}".format(P1.name, P1_Score))
        print("Final Score for {} is {}".format(P2.name, P2_Score))
        if P1_Score > P2_Score :
            print("{} is the WINNER!".format(P1.name))
        if P1_Score < P2_Score :
            print("{} is the WINNER!".format(P2.name))
        if P1_Score == P2_Score :
            print("it is a TIE!")    
    
    return P1_Score, P2_Score