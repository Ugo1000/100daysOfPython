''' with open we dont need to close the file'''

# with open("test.txt", mode="r") as myfile:
#     print(myfile.readlines())


# with open("test.txt", mode="w") as myfile:
#     print(myfile.write("Hey its e i'v written to file"))


# with open("test.txt", mode="r") as myfile:
#     print(myfile.readlines())

# with open("test.txt" , mode="r+") as myfile:
#     print(myfile.readlines())

with open("home/ugo/Desktop/UDEMY/Python/100daysOfPython/100DaysCodingPython/out.txt" , mode="w") as myfile:
    print(myfile.write("i wrote again"))