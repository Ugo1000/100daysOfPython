class Student:
    # class object attribute
    is_a_student = True

    def __init__(self, name, age):  # this is a constructor same way you give constructor in java

        if (Student.is_a_student):
            self.name = name  # self is the same as this.name in java
            self.age = int(age)

    def run(self):
            return ("Runnnig..")

    def shout(self):
            return (f"my name is {self.name}, i just shouted ")


student = Student("Nelly", 26)
student1 = Student("Frank", 28)


print(student1.shout())
print(f'student name is {student.name} and is {student.age} years old ')
# help(list)
