
class Portal:
    def __init__(self):
        self.name =''
    
    # Using @property decorator
    # Getter method
    @property
    def get_name(self):
        return self.name
    
    # Setter method
    @get_name.setter
    def set_name(self, val):
        self.name = val

    # Deleter method
    @get_name.deleter
    def delete_name(self):
       del self.name


p = Portal()
p.set_name = 'Ujjawal Patidar'
print (p.get_name)
del p.delete_name
# print (p.get_name)