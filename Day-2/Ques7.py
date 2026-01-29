# Find the common elements between two lists using sets.

l1 = [1,2,3,4,5,6,7,8]
l2 = [12,13,14,1,2,3,4,5]

print(set(l1) & set(l2))    # intersection
print(set(l1) | set(l2))    # union
print(set(l1) ^ set(l2))    # unique of both