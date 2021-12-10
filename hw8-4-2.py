# Author: JD 12/09/2021

from random import randint


def rock_paper_scissors():
    def game(player):
        """Play rock paper scissors"""
        computer = randint(0, 2)
    
        # Check if the user or the computer won.
        if player == computer:
            print("It's a tie!")
            return "tie"
        elif player == 0:
            if computer == 1:
                print("You lose, paper covers rock.\n")
                return "loss"
            else:
                print("You win, rock crushes scissors!\n")
                return "win"
        elif player == 1:
            if computer == 2:
                print("You lose, scissors cuts paper.\n")
                return "loss"
            else:
                print("You win, paper covers rock!\n")
                return "win"
        elif player == 2:
            if computer == 0:
                print("You lose, rock crushes scissors.\n")
                return "loss"
            else:
                print("You win, scissors cuts paper!\n")
                return "win"
 
        
    def play():
        scoreboard = []
        tie = 0
        win = 0
        loss = 0
        total = 0
        run = True
        while run == True:
            player = input("Enter 0 for rock, 1 for paper, and 2 for scissors: ")
            if player not in ["0", "1", "2"]:
                print("Invalid input.")
                continue
            player = int(player)
            result = game(player)
            total += 1
            scoreboard.append(result)
            condition = input("Do you want to play another round?(enter Y/N)").upper()
            if condition == "N":
                run = False
            else:
                run = True
        for x in scoreboard:
            if x == "tie":
                tie += 1
            elif x == "win":
                win += 1
            else:
                loss += 1
        resultboard=[tie, win, loss]
        print("We have played {0} games, we tied {1} times, you won {2} games, and you lost {3} games.".format(total, resultboard[0], resultboard[1], resultboard[2]))
    play()
play_game = rock_paper_scissors()
        
        

