# Create a dictionary from two lists (one for keys, one for values) using zip().

l1 = [1,2,3,4]
l2 = ["one", "two", "three", "four"]
d = {}

for key, value in zip(l1, l2):
    d[key] = value

print(d)