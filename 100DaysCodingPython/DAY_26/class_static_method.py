# Static method are define using @staticmethod
# and can be called directly without creating a class

class Myclass:
    class_variable = 10

    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method(x, y):
        return x + y


    # calling static without creating an instance of the class
result = Myclass.static_method(2, 5)
print(result)

class1 = Myclass(6)
print(class1.class_variable)
