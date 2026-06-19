# DAY 10 - Error Handling

# --- basic try/except ---
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That is not a number!")

# --- division error ---
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")

# --- finally block ---
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished!")

# --- practical example ---
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"

print(divide(10, 2))
print(divide(10, 0))