# DAY 15 - Mini Project: Student Grade Manager

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    def show(self):
        print(f"Name: {self.name} | Marks: {self.marks} | Grade: {self.get_grade()}")


def save_to_file(students):
    file = open("students.txt", "w")
    for s in students:
        file.write(f"{s.name},{s.marks},{s.get_grade()}\n")
    file.close()
    print("Results saved to students.txt!")


students = []

while True:
    print("\n1. Add student")
    print("2. Show all students")
    print("3. Save to file")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append(Student(name, marks))
        print("Student added!")

    elif choice == "2":
        if len(students) == 0:
            print("No students added yet!")
        else:
            print("\nAll Students:")
            for s in students:
                s.show()

    elif choice == "3":
        save_to_file(students)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again!")