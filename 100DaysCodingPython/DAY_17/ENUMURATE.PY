# for index,char in enumerate("HELLO WORLD"):
#     if char == 'L':
#         print(f'the index of {char} is {index}')


# for index,char in enumerate("SAMUEL".lower()):
#     if char == 'l':
#         print(f'the index of {char} is {index}')

for index,char in enumerate(range(1,100)):
    print(index,char)
    if char == 55: # this check the equality of the value.
        print(index,char)
        print(f'the index of {char} is {index}')

