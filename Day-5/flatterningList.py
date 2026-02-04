l = [1,2,[1,2,[1,2]], 3, 4, [6,7], [1,2,3,4,[1,2,3]]]

flat = []

def flatternList(l):
    
    for i in l:
        if(type(i) == list):
            flatternList(i)
        else:
            flat.append(i)

flatternList(l)
print(flat)