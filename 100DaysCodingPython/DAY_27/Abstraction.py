# Abstraction means hiding of information
# And giving access to only what's nesscary

# privat ?
class Player:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

    def run(self):
        # print(f'{self.name} is running')
        return (f'{self.name} is running')

    def speak(self):
        return (f'My name is {self.name}, and i am {self.age} years old and i posses {self.power} power')


player1 = Player("Odumodu", 50, "Thunder")
player1.name = "Anoynomous"

print(player1.name)
print(player1.run())
print(player1.speak())
player1.speak()

# player1.speak = "Balablu.....u"
# print(player1.speak)
