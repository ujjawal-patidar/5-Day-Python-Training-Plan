# Check if a given string is a palindrome (case-insensitive).

str = input("Enter your string : ")
n = len(str)

for i in range(0, len(str)//2):
    if(str[i].lower() != str[n - i - 1].lower()):
        print("Not Palindrome")
        break
    else:
        print("Palindrome")
        break


