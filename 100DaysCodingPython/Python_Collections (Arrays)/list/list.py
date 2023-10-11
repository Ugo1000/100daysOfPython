#!/bin/python3
# list/arrays in other programming language 

amazon_cart =  [ 'notebook' , 'sunglasses' , 'brewvergies']

print(amazon_cart)
print(amazon_cart[0])
print(amazon_cart[2])
print(amazon_cart[1])
print(f'i want the item {amazon_cart[1]} please get them for me ')


# you can use so many method with list 
amazon_cart.append("toy")

print(type(amazon_cart))# <class 'list'> 

# a list can contain diffrent data types 
amazon_cart.append(500)
amazon_cart.append(True)
print(amazon_cart)

# list collection
print(amazon_cart)

amazon_cart[0] = "TextBook"

newCart = amazon_cart
newCart[0] = 'gum'
print(newCart)
print(newCart)
