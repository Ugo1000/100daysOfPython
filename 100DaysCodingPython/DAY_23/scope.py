# The nonlocal keyword is used to refrence a variable in the nearest scope

def foo():
    # local variable of foo()
    name = "geek"
    # First inner function

    def bar():
        name = "Samuel Geek"
        # Second inner fuction

        def ack():
            nonlocal name  # refer to the nexted upper variable with this name
            print(name)
            name = "GEEK!!"
        ack()
    bar()
    print(name)


foo()
