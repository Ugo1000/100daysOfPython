from typing import Any


class Toy():
    myList = [10, 8, 7, 4, 3, 55, 89, 5, 4, 1, 2, 3, 10]

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dic = {
            'name': 'Transformer', 'prize': 50
        }

    def __str__(self):
        return f'{self.color, self.age}'

    def __len__(self):
        return 100

    # def __del__(self):
    #     print("Deleted!!")

    def __call__(self):
        return ("Yes , I'm here.")

    def __getitem__(self, index):
        return self.my_dic[index]


mytoy = Toy('Yellow', 2)
print(mytoy['name'])

