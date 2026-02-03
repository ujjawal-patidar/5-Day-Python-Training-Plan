# Implement a class with __str__ and __repr__ special methods for better debugging.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # it will define how humans see it
    def __str__(self):
        return f"({self.x}, {self.y})"

    # aur this will define how the interpreter sees it
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(1, 2)
print(p.__repr__())