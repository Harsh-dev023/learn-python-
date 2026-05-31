# DAY 4 - Loops

# --- for loop ---
print("--- for loop ---")
for i in range(1, 6):
    print("Number:", i)

# --- loop through a list ---
print("--- loop through list ---")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

# --- while loop ---
print("--- while loop ---")
count = 1
while count <= 5:
    print("Count:", count)
    count = count + 1

# --- practical example ---
print("--- multiplication table ---")
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number * i)