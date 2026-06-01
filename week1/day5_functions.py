# DAY 5 Functions

#functiON
def greet():
    print("Hello")

greet()

#INPUT
def greet_user(name):
    print("Hello,", name)

greet_user("Harsh")
greet_user("Nihal")

#RETURN
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(10, 20)
print("Sum:", answer)

#EXAMPLE
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

student_marks = int(input("Enter your marks: "))
grade = calculate_grade(student_marks)
print("Your grade is:", grade)