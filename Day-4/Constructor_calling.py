class A:
    def __init__(self, name):
        print("Hello")
        self.name = name
        print(self.name)
        # self.name = name
    
class B(A):
    def show():
        print("called B show")

a = B("Ujjawal")

