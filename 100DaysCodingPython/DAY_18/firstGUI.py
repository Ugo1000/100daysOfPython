# record = int(input("Enter the student record need to add :"))

# First Exercise
picture =[
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
empty= ' '
fill = '*'
for row in picture:
    for pixel in row:
        if pixel == 1:
            print(fill, end=empty)
        else:
            print(empty,end=' ')
    print(' ') # need a new line after every row.

    
