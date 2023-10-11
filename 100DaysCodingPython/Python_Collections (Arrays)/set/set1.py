set1 = {1,2,3,7,8,9,5}
print("the lenghth of set1 is ",len(set1),set1)
# set 2
set2 = {4,20,58,7,9,10,15}
print("The lenghth of set2 is ",len(set2),set2)

#conat the two sets
#sets  = set2 + set1 # which is not supportted
print()
set_diff = set1.difference(set2)
print()
print("set difference", set_diff)
print()
set1.discard(5)
print(set1)

# list can be converted to set 
my_list = [10,20,30,40,50,60]
print(type(my_list))
listConvert = set(my_list) # @ this point list was converted 
print(type(listConvert)) 
print()



# enter an input as a set 
var = input("Enter a string :")
varSet = set(var)
print(varSet)
convertedToString = str(varSet)
isLowercase = convertedToString.islower()
print("is the set a lower case  : ",isLowercase)
print('is "A" among what he/she typed ?? ')
print('a' in varSet)





