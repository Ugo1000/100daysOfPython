class Player:
    membership = True

    def __init__(self, name, age):
        # this is a constructor same way you give constructor in java
        if (self.membership):
            self.name = name  # self is the same as this.name in java
            self.age = int(age)

    def run(self):
        return ("Runnnig..")


player1 = Player("Ronaldo", 31)

print(f'player 1 name is {player1.name} and is {player1.age} years old ')
print(f'{player1.run()}')
