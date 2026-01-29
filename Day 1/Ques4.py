# Convert temperature from Celsius to Fahrenheit and vice versa.

temp = input("Enter the temperature with C or F at last that will be converted to another scale: ")
char = temp[len(temp) - 1]

temp = float(temp[:len(temp)-1])

if(char == 'c' or char == 'C'):
    f = (temp * 9/5) + 32
    print(f"In Fahrenheit {f} F")
elif(char == 'f' or char == 'F'):
    c = (temp - 32) * 5/9
    print(f"In Celsius {c} C")
else:
    print("Invalid Input")    

