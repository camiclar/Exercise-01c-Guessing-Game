#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

number = random.randrange(1,11)
numGuesses = 0
guess = input("Guess a number from 1 to 10 or type 'Quit' to exit: ")
while guess != "Quit":
    try:
        if int(guess) > number:
            guess = input("You guessed too high! Try a lower number or type 'Quit' to exit: ")
            numGuesses += 1
        elif int(guess) < number:
            guess = input("You guessed too low! Try a higher number. or type 'Quit' to exit: ")
            numGuesses += 1
        elif int(guess) == number:
            numGuesses += 1
            break
    except:
        guess = input("Your input wasn't recognized. Guess a number from 1 to 10 or type 'Quit' to exit: ")
        

if guess == str(number):
    print("Great job! You got it! It took you " + str(numGuesses) + " guesses to find the number.")
else:
    print("Thanks for plyaing! The number was " + str(number))