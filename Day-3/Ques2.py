# Create a function that returns the factorial of a number (both iterative and recursive).

def recursive_fact(n):
    if(n == 1 or n == 0):
        return n
    return n * recursive_fact(n-1)

def fact(n):
    if n == 1:
        return n  
    
    res = 1
    for i in range(2,n+1):
        res *= i
    
    return res

print(recursive_fact(3))
print(fact(3))