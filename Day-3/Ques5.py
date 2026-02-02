# Implement a function that uses map() and filter() together to process a list.

l = [1,2,3,4,5,6,7,8,9, 10]

new_l = map(lambda a : a * 2 ,filter(lambda a : a % 2 == 0, l))

for i in new_l:
    print(i)