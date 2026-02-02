# Create a function using **kwargs to create a student profile dictionary.

def create_dict(**kwargs):
    print(kwargs)


# create_dict(name = "Ujjawal", degree = "B.tech", college = "Medicaps University")
create_dict(student1 = {
    "name" : "Ujjawal",
    "roll no" : 1
}, stud2 = {
    "name" : "Anant",
    "roll no" : 2
}, stud3 = {
    "name" : "Vaibhav",
    "roll no" : 3
})