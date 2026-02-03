# Implement a class Stack with push, pop, peek operations and raise custom exceptions for overflow/underflow.

class StackOverFlow(Exception):
    pass

class StackUnderFlow(Exception):
    pass

class Stack:
    def __init__(self):
        self.st = []
    
    def push(self, value):
        self.st.append(value)
    
    def pop(self):
        try:
            if(len(self.st) == 0):
                raise StackUnderFlow("Stack underFlow...")
        except StackUnderFlow as err:
            print(err)
        else:
            return self.st.pop()

    def peek(self):
        try:
            if(len(self.st) == 0):
                raise StackUnderFlow("Stack underFlow...")
        except StackUnderFlow as err:
            print(err)
        else:
            return self.st[-1]
        # if(len(self.st) == 0):
        #     raise StackUnderFlow("Stack underFlow...")
        # return self.st[-1] 
    
    def __str__(self):
        l = []
        for i in range(len(self.st)-1,-1, -1):
            l.append(f"|{self.st[i]}|\n")
        return "".join(l)

st = Stack()
print(st.peek())
st.push(10)
st.push(20)
st.push(30)
print(st)
