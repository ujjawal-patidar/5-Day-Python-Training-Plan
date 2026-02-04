#In Python, NamedTuple is present inside the collections module. It provides a way to create simple, lightweight data structures similar to a class, but without the overhead of defining a full class. Like dictionaries, they contain keys that are hashed to a particular value. On the contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

# namedtuple(typename, field_names)

# typename - The name of the namedtuple. 
# field_names - The list of attributes stored in the namedtuple.

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', DOB='2541997')
A = Student('Ujjawal', '20', DOB='03032005')

# Now Access using index
print("The Student age using index is : ")
print(S[1])

print("The Student age using index is : ")
print(A[1])

# Access using name
print("The Student name and DOB using keyname is : ")
print(S.name, S[2])
print(A.name, A[2])

B = Student([1,3], [1,2], {'a' : 2})
print(B)
