# Write a function to check if a number is prime.

def is_prime(n):
    for i in range(2, n//2):
        if(n % i == 0):
            return False
    return True

print(is_prime(2))
print(is_prime(16))
print(is_prime(17))