# DAY 8 - Tuples and Sets

#TUPLES (cannot be changed) 
coordinates = (10, 20)
colors = ("red", "green", "blue")

print("Coordinates:", coordinates)
print("Colors:", colors)

#access tuple items 
print("First color:", colors[0])
print("Last color:", colors[-1])

#loop through tuple
print("--- all colors ---")
for color in colors:
    print(color)

#tuple length
print("Total colors:", len(colors))

#SETS 
numbers = {1, 2, 3, 4, 5}
print("Numbers:", numbers)

# dd to set
numbers.add(6)
print("After adding 6:", numbers)

# remove from set 
numbers.remove(3)
print("After removing 3:", numbers)

#sets remove duplicates automatically 
names = {"Harsh", "Nihal", "Harsh", "Ravi", "Nihal"}
print("Unique names:", names)

#  example 
student_marks = (85, 90, 78, 92, 88)
print("Marks:", student_marks)
print("Highest:", max(student_marks))
print("Lowest:", min(student_marks))
print("Total:", sum(student_marks))