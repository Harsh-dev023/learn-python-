# DAY 16 - Advanced String Formatting

name = "Harsh"
age = 20
marks = 85.5

# f-strings (modern way)
print(f"My name is {name} and I am {age} years old")
print(f"My marks are {marks:.1f}")

# format() method
print("My name is {} and I am {} years old".format(name, age))

# string methods
text = "  Python is Awesome  "
print("Original:", text)
print("Stripped:", text.strip())
print("Replace:", text.strip().replace("Awesome", "Fun"))
print("Split:", text.strip().split(" "))
print("Title case:", text.strip().title())

# checking strings
word = "Python"
print("Starts with Py:", word.startswith("Py"))
print("Ends with on:", word.endswith("on"))
print("Is digit:", word.isdigit())
print("Is alpha:", word.isalpha())

# joining strings
words = ["I", "love", "Python"]
sentence = " ".join(words)
print("Joined:", sentence)

# practical example - formatted receipt
item = "Notebook"
price = 49.999
quantity = 3
total = price * quantity
print(f"Item: {item}")
print(f"Price: Rs.{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: Rs.{total:.2f}")