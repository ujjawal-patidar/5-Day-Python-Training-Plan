# Implement a class with __getitem__, __setitem__, and __len__ to create a custom collection that behaves like a list.

class my_list:
    def __init__(self, *l):
        self.l = list(l)
    
    def __getitem__(self, idx):
        return self.l[idx]
    
    def __setitem__(self, idx, value):
        self.l[idx] = value
    
    def __len__(self):
        return len(self.l)
    
l = my_list(1,2,3,4,5)
print(l[0])
print()
l[1] = 20

for i in l:
    print(i , end = " ")


print()
print(l)