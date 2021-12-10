# Author: JD 12/09/2021

import random

def game():
    num = random.randint(0,50)
    guess = input('Guess the number (enter "stop" to end the game): ')
    if guess == "stop":
        print("You have ended the game, the number is {0}".format(num))
        return
    guess = int(guess)
    while guess != num:
        if guess > num:
            print("Go lower.")
        else:
            print("GO higher.")
        
        guess = input('Guess the number (enter "stop" to end the game): ')
        if guess == "stop":
            print("You have ended the game, the number is {0}".format(num))
            return
        guess = int(guess)
    print("You have won the game!")
    return

game()
