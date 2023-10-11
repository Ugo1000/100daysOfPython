class A:
    def method(self):
        print("Method in class A")


class B(A):
    def method(self):
        print("Method in class B")


class C(A):
    def method(self):
        print("Method in class C")


class D(C, B):
    pass


# print(D.__mro__)
d = D()
print(d.method())
