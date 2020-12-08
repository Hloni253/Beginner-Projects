#Number Guessing Game

import random

print("We are going to play a game")
answer = str(input("Do you want to play a game, type y for yes and n for no "))
if answer == 'y':
    print("Awesome let's do this")
    while True:
        guessed_num = int(input("I'm thinking of a number between 1 and 10 "))
        random_num = random.randint(1,11)
        if guessed_num == random_num:
            print("You are a genius")
            break
        else:
            print("You lose\nTry again")