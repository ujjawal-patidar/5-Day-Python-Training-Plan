
def isEven(num):
    return True if num % 2==0 else False

# print(isEven(0))

def sign(num):
    return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

# print(sign(0))


# print(help(sign))

# Using Tuple
n = 7
res = ("Odd", "Even")[n % 2 == 0]
print(res)

# Using Dictionary
a = 10
b = 20
ans = {True: a, False: b}[a > b]
print(ans)


# using lambda
a = 10
b = 20
ans = (lambda x, y: x if x > y else y)(a, b)
print(ans)