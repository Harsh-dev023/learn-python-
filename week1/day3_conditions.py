#day 3  if else condition

age = int(input("enter age"))
if age >= 18:
    print("adult")
elif age >=13:
    print("teenager")
else:
    print("child")


marks = int(input("enter your marks"))
            
if marks >= 90:
    print("grade:a")
elif marks >=75:
    print("grade:b")
elif marks >= 50:
    print("grade: c")
elif marks >= 40:
    print("grade : d")
else:
    print("grade:fail")
