# Write a program to swap two variables without using a third variable.

a = 10  #30
b = 20

print("Before: ",a, b)

a = a+b
b = a-b
a = a-b

print("After: ",a , b)
