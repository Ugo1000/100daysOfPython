class NameOfClass:
    class_attribute = 10

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # code
        return self

    @classmethod
    def cls_method(cls, par1, par2):
        # code
        return par1 + par2

    @staticmethod
    def static_method():
        # code
        return ("i'm static method")
        pass


class1 = NameOfClass(10,20)
class2 = NameOfClass(1,2)
class3 = NameOfClass(15,0)
print(class1.class_attribute)
print(class1.method())
print(class2.method())
print(class3.method())
print(NameOfClass.static_method())


