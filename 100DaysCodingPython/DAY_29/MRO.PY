# MRO = METHOD RESOLUTION ORDER
# This goes all the way through the inhenretance chain

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


d = D()
print(D.mro())
a = A()
print(a.num)
b = B()
print(b.num)
