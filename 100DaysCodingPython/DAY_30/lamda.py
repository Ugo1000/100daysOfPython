#!/usr/bin/python3

# Syntax
# lambda x : x * xt
import functools

number = [5, 4, 3]
num = [(1, 20), (10, 12), (1, -4)]
(num.sort(key=lambda x: x[1]))
print(num)

# sq = list(map(lambda item: , num))
