#!/bin/usr/python3
from random import randint

# takes the name of the player
name = input("Enter your name : ")
answer = randint(1, 10)
print(answer)

'''       
    This fuction takes
    param 1 : guess
    param 2 : answer
    param 3 : name

    retun the guess if it's equal answer

'''


def my_guess(guess, answer, name):
    if 0 < guess >= 11:
        print("Value must be between 1~10")
    if guess == answer:
        print(f"Damn!!! {name} you are a genius")
        return True
    else:
        return False


if __name__ == "__main__":

    # use exception
    while True:
        try:
            # input from user
            guess = int(input("What's your guess 1~10 : "))
            # check the input is number 1~10
            if my_guess(guess, answer, name):
                break

        except ValueError:
            print("Must be Number 1~10")
            continue
