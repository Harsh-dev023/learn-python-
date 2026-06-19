# DAY 17 - Lambda Functions

# normal function
def add(a, b):
    return a + b

print("Normal function:", add(10, 20))

# lambda function
add_lambda = lambda a, b: a + b
print("Lambda function:", add_lambda(10, 20))

# lambda with one argument
square = lambda x: x * x
print("Square of 5:", square(5))

# lambda with condition
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("10 is:", check_even(10))
print("7 is:", check_even(7))

# lambda with map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# lambda with filter
numbers = [10, 25, 30, 45, 50, 65, 70]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# lambda with sorted
students = [
    {"name": "Harsh", "marks": 85},
    {"name": "Nihal", "marks": 92},
    {"name": "Ravi", "marks": 78}
]
sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['marks']}")