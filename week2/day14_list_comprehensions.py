# DAY 14 - List Comprehensions

# normal way to create a list
numbers = []
for i in range(1, 11):
    numbers.append(i)
print("Normal way:", numbers)

# list comprehension way
numbers = [i for i in range(1, 11)]
print("Comprehension way:", numbers)

# squares of numbers
squares = [i * i for i in range(1, 11)]
print("Squares:", squares)

# even numbers only
evens = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers:", evens)

# odd numbers only
odds = [i for i in range(1, 21) if i % 2 != 0]
print("Odd numbers:", odds)

# uppercase names
names = ["harsh", "nihal", "ravi", "rohit"]
upper_names = [name.upper() for name in names]
print("Upper names:", upper_names)

# filter marks above 70
marks = [85, 45, 90, 60, 78, 35, 92]
passed = [m for m in marks if m >= 50]
print("Passed marks:", passed)
failed = [m for m in marks if m < 50]
print("Failed marks:", failed)

# practical example
prices = [100, 200, 300, 400, 500]
discounted = [p * 0.9 for p in prices]
print("Original prices:", prices)
print("After 10% discount:", discounted)