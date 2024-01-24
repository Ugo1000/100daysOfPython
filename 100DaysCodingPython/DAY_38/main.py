#!/usr/bin/python3

# HOC - higher order funtion :
# it's a funtion that accept func as param or return another funtion


# DECORATOR


def my_decorator(func):
    def wrap_func(*agrs):
        print("*****before*****")
        func(agrs)
        print("*****after*****")
    return wrap_func


@my_decorator
def greet(name):
    return f"HELLO {name}"


def main():
    data = greet("SAMUEL")
    print(data)


if __name__ == '__main__':
    main()
