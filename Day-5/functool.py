#functools is a module for the tools of higher order functions which takes or return functions

from functools import partial, lru_cache, reduce
import time

# def add(a,b,c,d):
#     return a , b , c , d

# new_add = partial(add, d=1,c=2, a=3)
# print(new_add(b=4))


@lru_cache(maxsize=128, typed = False)
def mul(x, y):
    time.sleep(2) 
    result = x * y
    return result

# The first call computes and caches the result
# print(mul(2, 3)) 


# print(mul(2, 3))  # The second call with the same arguments returns the cached result in instaltly

# print(mul('2', 3))


l = [1,2,3,4,5]
sum_result = reduce(lambda x, y : x + y, l, 1)   # -> reduce(function(with two args) , iterator[ , initiallation Value])
print(sum_result)

