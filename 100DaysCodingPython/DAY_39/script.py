#!/usr/bin/python3

import re

my_search_text = input("Enter text to search :  ")
my_str = "welcome hello to regular expressiion in python 3"

pattern = re.compile(my_search_text)
searched = pattern.search(my_str)

# pattern.findall()
# pattern.fullmatch() // The exact match
# pattern.match // partial match

while True:

	if searched:
    		print(f'{my_search_text} was found from the text ')
	elif:
    		print(f"{my_search_text} was not found ")
	else:
		break



# s = re.search("welcome", my_str)
# span = s.span()
# print(span)
# grp = s.group()
# print(grp)
# start = s.start()
# print(start)
# last = s.end()
# print(last)
# exp = s.expand("expanded")
# print(exp)
