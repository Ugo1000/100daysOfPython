def highest_even(args):
    even= []
    for theList in args:
        if theList % 2 == 0:
            even.append(theList)
    return max(even)

            


myList = [1,7,4,2,8,20,100,18,12]
print(type(myList))


print(highest_even(myList))