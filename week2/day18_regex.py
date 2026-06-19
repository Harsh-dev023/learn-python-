# DAY 18 - Regular Expressions

import re

# basic match
text = "My name is Harsh and I live in Chandrapur"
match = re.search("Harsh", text)
if match:
    print("Found:", match.group())

# find all numbers
text = "I scored 85 in Maths, 90 in Science and 78 in English"
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)

# find all words starting with capital
text = "Harsh lives in Chandrapur and studies at Raisoni College"
capitals = re.findall(r'[A-Z][a-z]+', text)
print("Capital words:", capitals)

# validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"

print(validate_email("harsh@gmail.com"))
print(validate_email("harshgmail.com"))
print(validate_email("harsh@gmail"))

# validate phone number
def validate_phone(phone):
    pattern = r'^\d{10}$'
    if re.match(pattern, phone):
        return "Valid phone number"
    else:
        return "Invalid phone number"

print(validate_phone("9876543210"))
print(validate_phone("98765"))
print(validate_phone("987654321a"))

# replace text
text = "I love Java and Java is great"
new_text = re.sub("Java", "Python", text)
print("Replaced:", new_text)

# split text
text = "Harsh,Nihal,Ravi,Rohit"
names = re.split(",", text)
print("Names:", names)