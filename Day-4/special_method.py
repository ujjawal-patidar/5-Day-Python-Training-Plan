class CustomList:
    def __init__(self):
        self.data = []
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def append(self, val):
        self.data.append(val)

    def __getitem__(self, key):
        return self.data[key]
    
    def __str__(self):
        return f"{self.data}"

my_list = CustomList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list[0])
print(my_list[1])
print(my_list[2])
