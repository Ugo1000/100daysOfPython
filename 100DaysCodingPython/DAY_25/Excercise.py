class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("puppy", 5)
cat2 = Cat("smokey", 7)
cat3 = Cat("lupy", 8)

# print(cat1.age)
# print(cat2.age)
# print(cat3.age)

myCatAge = [cat1.age, cat2.age, cat3.age]
# print(type(catsAge))


def oldest(cat_age):
    oldAGE = []
    for cat in cat_age:
        if cat > 0:
            oldAGE.append(cat)
    return max(oldAGE)


print(f"The oldest cat is {oldest(myCatAge)} years old.")
