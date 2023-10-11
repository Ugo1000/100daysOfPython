class User:
    def sign(self):
        print("Logged in")
    # even if the  base class has an attack method the sub class overide them

    def attack(self):
        print(f"attacking with power of {self.power} from base class")


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


wiz = Wizard('merlin', 'bowl')
arc = Archor("harry", "fuzzzz")


arc.attack()
wiz.attack()
