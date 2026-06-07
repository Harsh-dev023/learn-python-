# DAY 11 - Classes and Objects

# create a class 
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def greet(self):
        print("Hello, my name is", self.name)

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Grade:", self.get_grade())

# create objects 
student1 = Student("Harsh", 20, 85)
student2 = Student("Nihal", 21, 92)

# use the objects
student1.greet()
student1.show_details()

print()

student2.greet()
student2.show_details()