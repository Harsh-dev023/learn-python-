# DAY 7 Dictionaries

#create a dictionary 
student = {
    "name": "Harsh",
    "age": 20,
    "city": "Chandrapur",
    "college": "Raisoni"
}

#  print dictionary 
print("Student:", student)

# access values 
print("Name:", student["name"])
print("Age:", student["age"])

# add a new key 
student["marks"] = 85
print("After adding marks:", student)

# update a value
student["age"] = 21
print("After updating age:", student)

#  remove a key 
del student["city"]
print("After removing city:", student)

# loop through dictionary 
print("--- all details ---")
for key, value in student.items():
    print(key, ":", value)

# xample 
phone_book = {
    "Harsh": "9876543210",
    "Nihal": "9123456789",
    "Ravi": "9012345678"
}

name = input("Enter name to search: ")
if name in phone_book:
    print("Phone number:", phone_book[name])
else:
    print("Name not found!")