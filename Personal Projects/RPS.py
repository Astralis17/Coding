import random
#               Rock,   Paper, Scissors
Conditions = [[0,-1,1],[1,0,-1],[-1,1,0]]
Options = ["Rock", "Paper", "Scissors"]

wins   = 0
losses = 0
draws  = 0
run = True



def challenge(condition, oppMove):
        x = condition[oppMove]

        # Draw
        if x == 0:
                print("You drew")
                return 1, 0, 0
        # Win
        elif x > 0:
                print("You win")
                return 0, 1, 0
        # Loss
        else:
                print("You lost")
                return 0, 0, 1


while run:

        print("Rock, Paper, Scissors, now we show")
        choice = input()

        if choice.capitalize().startswith("R"):
                choice = 0

        elif choice.capitalize().startswith("P"):
                choice = 1

        elif choice.capitalize().startswith("S"):
                choice = 2

        print("You chose ", Options[choice])

        oppMove =  random.randint(0, 2)

        oppMove = 2
        print("Opponent chose ", Options[oppMove])

        result  = challenge(Conditions[choice], oppMove)
        draws  += result[0]
        wins   += result[1]
        losses += result[2]

        if wins == 2:
                run = False
                print("You Won overall, you won ", wins, " times, drew ", draws, " times and lost ", losses, " times")
        elif losses == 2:
                run = False
                print("You lost overall, you won ", wins, " times, drew ", draws, " times and lost ", losses, " times")