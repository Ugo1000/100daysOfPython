# THIS A GUESS GAME FROM THE TERMINAL
#!/usr/bin/python3

# import sys
import sys

# import random module

from random import randint

# input from the terminal

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        # input from user
        guess = int(input("What is your guess : "))
        # check input  is number 1~10
        if 0 < guess < 11:
            if guess == answer:
                print(f"Damn!!! you are a genius")
                break
        else:
            print("tozooo i said 1~10")
    except ValueError:
        print("Must be Number 1~10")
