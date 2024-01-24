#!/usr/bin/python3
import random
import time

name = input("Enter Name : ")
password = input("Enter password : ")
password_len = (len(password))
print(password_len)

if password_len == 8 and password is not None :
	print("correct password")
else:
	print("Not correct")

print("The program generate random number between 1~90")
num1 = random.randint(1,90)
time.sleep(1)
num2 = random.randint(1,90)
time.sleep(1)
num3 = random.randint(1,90)
time.sleep(1)
print(f'{name} your number are')
print({num1},{num2},{num3})
