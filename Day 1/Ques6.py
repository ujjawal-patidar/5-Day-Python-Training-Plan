# Count the frequency of each character in a string using a dictionary.

str = input("Enter the string : ")

d = {}

# for i in str:
#     if d.get(i):
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

for i in str:
    d[i] = str.count(i)

print(d)