'''     POLYMORPHISM 
    calling the base class with the  super method without passing self
'''
class User:
    def __init__(self, email):
        self.email = email

    def sign(self):
        print("Logged in")
    # even if the  base class has an attack method the sub class overide them

    def attack(self):
        print(f"attack with nothing from base class")
# end of base class


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)  # with super you achive the same  as User.__init__(self, email)

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


wiz = Wizard('merlin', 'bowl', 'sam.com')
print(wiz.email)
arc = Archor("harry", "fuzzzz")


# arc.attack()
wiz.attack()
