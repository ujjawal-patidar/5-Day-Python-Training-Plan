import sys

# print(6 & 3)
# print(6 | 3)
# print(6 ^ 3)
# print(~3)
# print(6 << 2)
# print(6 >> 2)

print(sys.getsizeof(2))       #28 byte
print(sys.getsizeof(""))      # 41 byte
print(sys.getsizeof("32"))    # 1 char 1 byte
print(sys.getsizeof("Ujjawal"))    
print(sys.getsizeof([]))        #56
print(sys.getsizeof([1,2,3, "Ujjawal"]))   # one element is taking 8 byte to storing its address
# print(88 - 56)