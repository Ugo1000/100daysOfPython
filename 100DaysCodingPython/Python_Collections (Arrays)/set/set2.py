my_set = {1,2,3,55,98}
your_set = {1,2,3,4,5,6,7}
print("difrences" , my_set.difference(your_set))
#print("a number was discard " ,your_set.discard())
print("your_set", your_set) 
print("the intersection between this set are ",my_set.intersection(your_set))
print('does this set has something in common',my_set.isdisjoint(my_set))
print("the union of ", (my_set | your_set))
print("the union of ", (my_set.union(your_set)))
print("Intersect is the common value between my_set and your set ", my_set.intersection(your_set))
print(my_set.isdisjoint(your_set)) # return True if they share something common
print(your_set.issubset(my_set)) 
print(your_set.issuperset(my_set))
print(my_set.issuperset(your_set))