# python 3.8
# number guessing game

# import module that allows random number generating
import random

# create variable to gen no. between 1-00, set guess & counter var to zero
number = random.randint(1, 100)
guess = 0
counter = 0


# while the guess from user is not equal to zero, request a guess
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    counter += 1
# if guess is the same as generated number, print that they are correct
    if guess == number:
        print("You guessed correctly!")
# else if guess is higher than the gen number, print they guessed too high
    elif guess > number:
        print("Too high!")
# else, tell the user they guessed too low
    else:
        print("Too low!")


