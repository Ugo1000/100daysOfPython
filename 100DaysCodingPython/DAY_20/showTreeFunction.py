picture =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def showTree():
    empty= ' '
    fill = '*'
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print(fill, end= ' ')
            else:
                print(empty,end=' ')
        print(' ') # need a new line after every row.


showTree()
showTree()

# print(showTree()) ->  this print the location of this function in the memory.
