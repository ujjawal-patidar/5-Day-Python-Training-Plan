# Write a program to check if a year is a leap year.

year = int(input("Enter the year : "))

# if year % 400 == 0:
#     print("laep year")
# elif year % 100 == 0:
#     print("non-leap year")
# elif year % 4 == 0:
#     print("leap year")
# else:
#     print("Non-leap year")

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("leap year")
else:
    print("Not leap year")