class ToyBox:
    total_toys = 20

    def __init__(self, toy_name):
        self.toy_name = toy_name
        ToyBox.total_toys += 1

    @staticmethod
    def static_method(x, y):
        return x + y

    @classmethod
    def class_method(cls):  # cls mean the class
        return cls.total_toys

    def run(self):
        return "Running"


# Lets use the static methods 5nd class method
print(ToyBox.static_method(5, 3))

toy1 = ToyBox("Teddy")
toy2 = ToyBox("Mark")
toy3 = ToyBox("James")

# count the the instance of the class created. >> 23
print(f"The Total box created is : {ToyBox.class_method()}")
print(f'{toy1.toy_name} is {toy1.run()}')
