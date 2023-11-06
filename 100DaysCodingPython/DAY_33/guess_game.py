#!/usr/bin/python3

# import random module

from random import randint

answer = randint(1, 10)
print(answer)
name = input("Enter your name : ")
# use exception
while True:
    try:
        # input from user
        guess = int(input("What's your guess 1~10 : "))
        # check input  is number 1~10
        if 0 < guess >= 11:
            print("Value must be between 1~10")
        if guess == answer:
            print(f"Damn!!! {name} you are a genius")
            break
    except ValueError:
        print("Must be Number 1~10")
        continue
