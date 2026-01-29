# Write a program to find the second largest number in a list without sorting.
import sys

f = s = None
max = sys.float_info.min
print(sys.float_info)

l = [1,2,3,4,2,5,7,3,4]

for i in l:
    if max < i:
        s = f
        f = i
        max = i

print("Second largest : ", s)
