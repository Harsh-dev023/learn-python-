# DAY 9 - File Handling

# --- write to a file ---
file = open("notes.txt", "w")
file.write("My name is Harsh\n")
file.write("I am learning Python\n")
file.write("Today is Day 9\n")
file.close()
print("File written successfully!")

# --- read from a file ---
file = open("notes.txt", "r")
content = file.read()
file.close()
print("--- File Content ---")
print(content)

# --- read line by line ---
file = open("notes.txt", "r")
print("--- Line by Line ---")
for line in file:
    print(line.strip())
file.close()

# --- append to a file ---
file = open("notes.txt", "a")
file.write("File handling is easy!\n")
file.close()
print("Line added successfully!")

# --- read again to see changes ---
file = open("notes.txt", "r")
print("--- Updated File ---")
print(file.read())
file.close()