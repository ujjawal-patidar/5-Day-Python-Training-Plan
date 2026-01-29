# Print the first 10 numbers in the Fibonacci sequence using a while loop.

def gen(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b , a+b

for i in gen(10):
    print(i, end = ' ')

print()