# Iterable is object or collection that can be iterated over 
# example -> list , dictionary , tuple ,set ,string 
# it can also be looping over something 
# object in python can be iterable 
# the below methods are mostly used in iterating over in dictionary  

user = {
    'name': "Golaem",
    'age' : 50,
    'can_swim' : False
}

for key,values in user.items(): # used this when your printing values and keys
    print(key,values)

for items in user.items():
    print(items)

for values in user.values():
    print(values)

for keys in user.keys():
    print(keys)