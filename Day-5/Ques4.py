# Use Counter from collections to find the 3 most common elements in a list.

from collections import Counter

l = [1,2,3,1,2,3,1,1,2,2,4,5,6]

c = Counter(l)
print(c.most_common(3))
