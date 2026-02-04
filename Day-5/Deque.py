from collections import deque 
    
d = deque({1,2,3})  
a = [2,3,4]
print(d)

d.remove(2)
print(d)

d.append(2)
d.appendleft(0)
d.extend(a)

d.extendleft(a)
print(d)

# pop()  -> right side se
# popleft()  -> left side se


print(d[0])  
print(d[-1]) 


d.rotate(2)  #rotate the deque 2 steps to right
print(d)

d.rotate(-3) #Rotate deque 3 steps to the left
print(d)