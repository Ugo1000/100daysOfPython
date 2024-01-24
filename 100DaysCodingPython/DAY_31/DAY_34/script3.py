'''Try except block with file '''
    # Try pathlib module


try:
    with open('sad.txt', mode="x") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("file does not exists")
    raise err
except IOError as err: 
    print("Io error")
    raise err