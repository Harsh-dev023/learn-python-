# DAY 12 - Inheritance

# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# child class
class Student(Person):
    def __init__(self, name, age, marks, college):
        super().__init__(name, age)
        self.marks = marks
        self.college = college

    def show_details(self):
        super().show_details()
        print("Marks:", self.marks)
        print("College:", self.college)

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

# another child class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_details(self):
        super().show_details()
        print("Subject:", self.subject)

# create objects
student = Student("Harsh", 20, 85, "Raisoni")
teacher = Teacher("Mr. Kumar", 35, "Python")

# use the objects
student.greet()
student.show_details()
print("Grade:", student.get_grade())

print()

teacher.greet()
teacher.show_details()