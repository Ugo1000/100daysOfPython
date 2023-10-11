# Check for duplicate in the list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
mylist = []

# print the duplicate value
# CORECTION

for values in some_list:
    if some_list.count(values) > 1:
        mylist.append(values)

print(mylist)
