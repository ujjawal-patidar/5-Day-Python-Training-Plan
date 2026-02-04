# Counter will create a dictionary of element : Frequency

#The collections.Counter in Python is a specialized dict subclass used for counting hashable objects. It stores elements as dictionary keys and their counts as corresponding values. It is part of Python's standard collections module. 

from collections import Counter

c = Counter(['apple', 'banana', 'apple', 'orange', 'apple'])

for i, j in c.items():
    print(i, j)

print(c.most_common(1))   # [('apple', 3)]

for i in c.elements():
    print(i)

c.update(apple=3, banana=1, ginger = 2)    # add these values to existing counts

for i, j in c.items():
    print(i, j)

c.subtract(a=1, b=3)

# for i, j in c.items():
#     print(i, j)
print(c)
# print(c.total())

# arithemetic operations
# Arithmetic and Set Operations: Counter supports standard mathematical operations like addition (+), subtraction (-), intersection (&), and union (|). These operations only keep elements with positive counts in the resulting Counter.
d = Counter(apple = 1, banana = 3)
print(c + d)   # union
print(c & d)   # intersection