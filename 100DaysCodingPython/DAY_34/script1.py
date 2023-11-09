my_file = open("test.txt")

print(my_file.read())
# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>
print(my_file.read())
my_file.seek(0)
print(my_file.read()) 

print(my_file.readline)
print(my_file.readlines)

