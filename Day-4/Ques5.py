# Create a base class Animal and derived classes Dog and Cat with method overriding for make_sound().

class Animal:
    def __init__(self):
        pass

    def make_sound(self):
        print("No sound")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Bhow Bhow...")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("meao meao...")

c = Cat("kitty")
c.make_sound()

d = Dog("bonny")
d.make_sound()


