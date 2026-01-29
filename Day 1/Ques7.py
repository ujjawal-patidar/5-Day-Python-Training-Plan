# Write a program to format a string using all three formatting methods (%, .format(), f-strings).

name = input("Enter your name : ")
age = int(input("Enter your age : "))

# Format string
print(f"Name : {name} and Age : {age}")

# using %
print("Name : %s and Age : %s "%(name, age))

# using format method
print("Name : {name} and Age : {age:.2F} ".format(name = "Anant",  age = 17))