#!/bin/python3

basket = [100,11,2,3,310,8,3,65,1,9]

#adding
basket.append("one")
print(basket)
print(basket.index(310))
print('d' in basket)
print('one' in basket)
print(basket.count(3))
#print(basket.sort())
print(basket)
basket.pop()
print(basket)
newList = sorted(basket)
print('old list')
print(basket)
print("new list")
print(newList)
copiedList = basket.copy()
print(f'copied of the original is + {copiedList}')
basket.reverse()
print(basket)
