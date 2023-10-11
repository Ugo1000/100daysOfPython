
# Wrap the above code  in a function called checkDrive

def checkDrive(age):
    age = input("What is your age ? ")
    valid_age = int(age)

    if valid_age > 18:
        print("Powering On, Enjoy your ride! ")
    elif valid_age == 18 :
        print("Congratulations on your first year of driving, Enjoy your ride !!")
    else:
        print("Sorry you are too young to drive this. powering off... ")

checkDrive(20)

