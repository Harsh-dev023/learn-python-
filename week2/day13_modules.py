# DAY 13 - Modules and Libraries

# math module
import math

print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Power of 2^10:", math.pow(2, 10))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.9:", math.floor(4.9))

# random module
import random

print("Random number 1-10:", random.randint(1, 10))
print("Random choice:", random.choice(["apple", "banana", "mango"]))

# datetime module
import datetime

today = datetime.date.today()
print("Today's date:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))

# os module
import os

print("Current directory:", os.getcwd())

# practical example
print("Lucky number today:", random.randint(1, 100))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("Study day:", random.choice(days))