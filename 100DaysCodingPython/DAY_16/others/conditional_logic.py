is_old = 18
isLicenced = True


name = ("What is your name : ")
surname = ("What is your surname : ")
age = str("What year were you born ?  : ")
licensed = bool("Licenced , True/False")


if age >= is_old and isLicenced:
    print("You are qualify to drive")
elif age <= is_old:
    print("You are not mature enough for driving")
elif isLicenced != licensed:
    print("Get a Licence to qualify ")
else:
    print("Sorry you cant drive!!")
