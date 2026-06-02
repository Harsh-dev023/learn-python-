# DAY6 Lists

#create a list
fruits = ["apple", "banana", "mango", "orange"]
numbers = [10, 20, 30, 40, 50]

#print list
print("Fruits:", fruits)
print("Numbers:", numbers)

#access items 
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

#add items
fruits.append("grapes")
print("After adding:", fruits)

#remove items
fruits.remove("banana")
print("After removing:", fruits)

#loop through list
print("--- all fruits ---")
for fruit in fruits:
    print(fruit)

#list length
print("Total fruits:", len(fruits))

#practical example
marks = [85, 90, 78, 92, 88]
print("All marks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average mark:", sum(marks) / len(marks))