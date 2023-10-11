
class Player:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    def run(self):
        # print(f'{self.name} is running')
        return (f'{self.name} is running')

        # age() is not callable.
    def age(self):
        print(f'I am {self.age} years old')

    def speak(self):
        return (f'My name is {self.name}, and i am {self.age} years old and i posses {self.power} power')


player1 = Player("Abija", 45, "Light")
player2 = Player("Odumodu", 50, "Thunder")


print(player1.run())
print(player2.run())
print(player1.speak())

