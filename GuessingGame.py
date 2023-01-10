#Melissa Radford
#CIS 261
#Guessing Game

import random

def display_title():
    print('Guess the number! ')
    print()

def play_game(LIMIT):
    number = random.randint(1, LIMIT)
    print(f'Im thinking of a number from 1 to {LIMIT}\n')
    count = 1
    guess = int(input('Your guess:  '))

    while (guess != number):
        if guess < number:
            print('Too low.  ')
            count += 1
        elif guess>number:
            print('Too high.  ')
            count += 1
        guess = int(input('Your guess:  '))

    print(f'You guessed it in {count} tries. \n')

def main():
    display_title()

again = 'y'

while again.lower() == 'y':
    LIMIT = int(input('Enter the limit:  '))
    play_game(LIMIT)

    again = input('Do you want to play again? (y/n):  ')
    print()

print('Goodbye!  ')




