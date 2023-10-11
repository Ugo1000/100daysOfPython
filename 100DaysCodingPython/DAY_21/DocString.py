# Docstring give you more info about a function or code 
# With just a glance 

def mul(a,b):
    '''
    This multiply any integer arguments pass to it .
    '''
    return a * b

# print (mul(10,5))

# clean code 
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
 
# print(is_even(1))
# print(is_even(8))
# print(is_even(9))
# print(is_even(5))


# *args and **kwargs also know as  -->> Abitrary Arguments 
def super_func(*args):
    print(type(args))
    total = 0
    for items in args:
        total+= items
    print(total)
 
super_func(50,10,100)

def team(**kwargs):
    print(type(kwargs))
    for key ,value in kwargs.items():
        print('{} {}'.format(key,value))

team(name='samuel',age=25,course='computer scien')

def my_args_function(*args,**kargs):
    print(type(args))
    for member in args:
        print(member)
    for k,v in kargs.items():
        print(f'{k} {v} in the items' )


my_args_function('faith','chima',name='blessing', age=19)