# Note: dictionary is an unorder keys in the memory 

'''
dictionary = {
    'a': 1,
    'b': 9,
    'c': 7,
    'g' : 50 
}

print(dictionary['c'])
print(dictionary['a'])
print(dictionary['g'])
print(dictionary['c'])


'''

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

'''
print(thisdict)
print(len(thisdict))
print(type(thisdict))

'''
thisdict = dict(name = "John", age = 36, country = "Norway")

# print(36 in thisdict.values())
#print(thisdict.items())

#print(thisdict.clear())

#print(thisdict.popitem())
print(thisdict)
#print(thisdict.pop('name'))
'''
print(thisdict)
print(thisdict.popitem())
print(thisdict.popitem())
print(thisdict)
'''

Car =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

Car2 = Car.copy()
print('This a copy of  car2', Car2)
print(Car.get('prize', '$200')) # return key inputed if not exit
Car2.update({'year' : 2020})
print(Car2)

#del Car2 # this also python function



print(Car2)
for car_values in Car.values():
  print("This are the values from the Car2" ,car_values)

for car_keys in Car2.keys():
  print("This are the keys from the car2" ,car_keys)


