#!/usr/bin/python3


from random import randint

# Take user's name as input
name = input("Enter your name: ")

# Generate three random integers between 1 and 90 (inclusive)
num1 = randint(1, 90)
num2 = randint(1, 90)
num3 = randint(1, 90)

# Print the generated numbers along with the user's name
print(f"Hi {name}, your numbers are: {num1}, {num2}, {num3}")
