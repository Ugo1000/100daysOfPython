# used to encapusalate a statement
# it a sign variable to a larger expression
# And how to check new fetures in python

a = 'good morning ofit'
a.capitalize()

if ((n := len(a)) > 10):
    print(f"too long {n} element ")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
