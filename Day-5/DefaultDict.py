# The collections.defaultdict in Python is a dictionary subclass that provides a default value for a key that does not exist, eliminating the need to check if a key is present before using it and preventing a KeyError. 

#default_factory: When you create a defaultdict, you pass a "default factory" as an argument. This is a callable (like a function or a type such as int, list, set, or str) that takes no arguments and returns the default value for a missing key.

#Automatic Value Creation: When you try to access or modify a non-existent key, the defaultdict automatically calls the default_factory to create a new key-value pair with the missing key and the default value.

from collections import defaultdict


from collections import defaultdict

a = [1,1,2,3,2,3]

map = defaultdict(int)
for item in a:
    map[item] += 1

print(map)

for key, value in map.items():
    print(key, value)