#!/bin/usr/python3
from random import randint


name = input("Enter your name : ")
answer = randint(1, 10)
print(answer)


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
