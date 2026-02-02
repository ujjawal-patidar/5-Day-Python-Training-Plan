# Implement a decorator function that measures the execution time of other functions.
import time

def dec_time(func):
    def wrapper_func(a,b):
        t1 = time.time()
        time.sleep(5)
        ans = func(a,b)
        time_taken = time.time() - t1
        print(f"time taken : {time_taken}")
        return ans
    return wrapper_func

@dec_time
def add(a,b):
    return a+b

print(add(2,3))
# print(help(time.time))

# def sum():
#     time.sleep(5)
#     print("clled")

