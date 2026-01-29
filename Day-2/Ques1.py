# Write a program to print all even numbers from 1 to 100 using a for loop.

def gen(n):
    for i in range(2, n+1, 2):
        yield i

for i in gen(100):
    print(i)