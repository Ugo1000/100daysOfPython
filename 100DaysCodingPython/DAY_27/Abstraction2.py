class Myclass():
    def __init__(self):
        self._private_var = 42

    def get_private_var(self):
        return self._private_var

    def set_private_var(self, value):
        self._private_var = value


obj = Myclass()
print()
obj.set_private_var(20)
# obj._private_var = 15
print(obj.get_private_var())
# print(obj._private_var)