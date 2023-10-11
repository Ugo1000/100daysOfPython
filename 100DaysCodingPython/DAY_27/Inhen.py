class User:
    def sign(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archor(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with power of {self.num_arrows}")


wizard = Wizard('Aojo', 20)
print(wizard.sign())
wizard.attack()


is_wizz = (isinstance(wizard, object)) 
is_subclass = (issubclass(wizard, object)) 
is_wizz = (isinstance(wizard, Wizard)) 

if is_wizz:
    print(f"The {wizard.name} is a wizard class.")
elif is_subclass:
    print(f"{wizard.name} is a sub class ")
else:
    print(f"{wizard.name} is not a class")
