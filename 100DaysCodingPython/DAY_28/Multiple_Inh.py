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


class Borg (Wizard, Archor):
    def __init__(self, name, num_arrows, power):
        Archor.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


borg = Borg("badman", "thuder", 5)
borg.attack()
borg.sign()
print(borg.name)
print(borg.num_arrows)
