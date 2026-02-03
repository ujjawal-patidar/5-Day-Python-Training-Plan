# Create a class Student with class variable to count the total number of students created.

class Student:
    count_student = 0

    def __init__(self, name):
        self.name = name
        Student.count_student += 1
    
    #  @property
    def get_name(self):
        return self.name
    
    # @get_name.setter
    def set_name(self, new_name):
        self.name = new_name
    
    my_name = property(get_name, set_name)

ujjawal = Student("Ujjawal")
Anant = Student("Anant")

ujjawal.my_name = "Mahendra"
print(ujjawal.my_name)

print(Student.count_student)
