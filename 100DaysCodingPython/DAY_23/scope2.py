def foo():
    name = "geek global "

    def bar():
        global name
        name = "Samuel's Geek"  # Overwrite the global variable
        print(name)
    bar()
    print(name)


foo()
