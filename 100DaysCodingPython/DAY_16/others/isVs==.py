#  teh double equal == check for values
print(True == 1) # bool(1) which is true
print('' == 1) # '1' is a string and the later is a int
print ([] == 1) # [] is a falsy value
print(10 == 10.0)
print([] == [])

print()
# IS, checks for equality of values in same location in memory
print(True is 1) 
print(1 is 1) 
print ([] is 1) 
print(10 is 10.0)
print([] is [])
print([123] is [123])

a = [10 ,15, 20]
b = [10 ,15, 20]

print()
print(a == b)
print(a is b)
# print(z is b)
# print(z is b)


