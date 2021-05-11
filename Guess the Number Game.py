"""
This a cool and simple game which selects a number and asks the user to guess it.
"""

import os
import random
from time import sleep

def main():

    option = input('Welcome to GUESS THE NUMBER GAME\n\nSelect level of difficulty\nL for Low\nM for Medium\nH for High\
        \n\n\tEnter L/M/H : ')
    if option.lower() == 'l':
        x = 10
    elif option.lower() == 'm':
        x = 100
    elif option.lower() == 'h':
        x = 1000
    
    play(x)
    
    sleep(5)

def play(x):
    randomNumber = random.randint(1, x)
    guess = 0
    print(f'\nYour computer\'s AI randomly selected a number between 1 and {x}. You have to guess the number and find it out.\n')
    while guess != randomNumber:
        guess = int(input(f'\nEnter a number between 1 and {x}: '))
        if guess < randomNumber:
            print('Oops ! Guess again. Number too LOW.')
        elif guess > randomNumber:
            print('Oops ! Guess again. Number too HIGH.')
    
    print(f'\nYay ! Congrats, you won finally. The correct number was {randomNumber}\n\n\tGOOD BYE !!')

if __name__ == '__main__':
    main()