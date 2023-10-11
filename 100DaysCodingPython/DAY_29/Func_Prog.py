'''
    what is function programming is about seperation of concern
    that each funtion concern just one part 

    This quit diffrent from OOP were data are bind the an object .

'''


# def mul_by_3(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 3)
#     return print(new_list)


# mul_by_3([2, 3, 6])

# MAP,FLITER, ZIP AND REDUCE
from functools import reduce

my_number = [20, 30, 14, 21, 89, 20, 4, 6, 3]
num = [1, 2, 3]
test = 1, 2, 3, 4, 5

def mul_by_3(item):
    return (item * 3)


def odd_number(item):
    return (item % 2 != 0)


def accumulator(acc, item):
    # print(acc, item)
    return item + acc

print(tuple(zip(my_number, test)))

print(reduce(accumulator, test))

print(list(map(mul_by_3, num)))

print(list(filter(odd_number, my_number)))
