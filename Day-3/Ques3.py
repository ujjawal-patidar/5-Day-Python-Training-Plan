# Write a function that takes variable number of arguments (*args) and returns their average.

def average(*args):
    return sum(args) / len(args)


print(average(1,2,3,4,5))