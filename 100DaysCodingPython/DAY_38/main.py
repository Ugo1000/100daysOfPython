#!/usr/bin/python3

# HOC - higher order funtion :
# it's a funtion that accept func as param or return another funtion


# DECORATOR


def my_decorator(func):
    def wrap_func():
        print("*****before*****")
        func()
        print("*****after*****")
    return wrap_func


@my_decorator
def greet():
    print("HEllooo..")

def main():
    greet()
    

if __name__ == '__main__':
    main()
