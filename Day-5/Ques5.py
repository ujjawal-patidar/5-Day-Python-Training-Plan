# Create a decorator that caches function results (memoization) using a dictionary.

from collections import defaultdict

def cache_dec(func):
    d = defaultdict(dict)

    def wrapper(*args):
        print(d)
        if(d[(args)] == {}):
            d[(args)] = func(*args)

        
        return d[(args)]
    return wrapper

@cache_dec
def add(a,b):
    return a+b

@cache_dec
def mul(a,b):
    return a*b

print(add(5, 4))
print(add(5, 4))
print(add(4, 4))
print(add(4, 4))
print(mul(5, 4))
print(mul(5, 4))