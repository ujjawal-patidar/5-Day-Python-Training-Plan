# The itertools module in Python is a standard library module that provides a set of fast, memory-efficient tools for creating
# and manipulating iterators. It is designed to handle large datasets efficiently by processing items one at a time rather
# than loading them into memory. Key functions include infinite iterators (count, cycle, repeat), finite iterators (chain,
# zip_longest), and combinatoric iterators (product, permutations, combinations). 

import itertools as it

# for i in it.count(10,2):
#     print(i)


l = [1,2,3,4]

# for i in it.cycle(l):
#     print(i)

# for i in it.repeat(l, 3):
#     print(i)


l2 = [1,2,3,4,5, [2,3]]
d = {'a' : 1, 'b' : 2}

# print(it.chain(l, l2))
# for i in it.chain(l, l2, d):
#     print(i)

l = [1,2,3,4,5]
l1 = [1,2]

# for i in it.product(l,l1, repeat = 2):
#     print(i)

# for i in it.combinations(l, r = 2):
#     print(i)

for i in it.permutations(l, r = 2):
    print(i)