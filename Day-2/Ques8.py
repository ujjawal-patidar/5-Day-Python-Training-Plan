# Implement a basic phonebook using a dictionary (add, search, delete, update contacts).

import uuid

class PhoneBook:
    phoneBook = {}

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.id = self.__gen_uuid()
        
        self.__add(self.id, name, phone_number)
        
    
    def __gen_uuid(self):
        return str(uuid.uuid4())
    
    def __add(self, id, name, phone_number):
        PhoneBook.phoneBook[id] = [name, phone_number]
    
    def update(self, updated_phone_number):
        PhoneBook.phoneBook[self.id][1] = updated_phone_number
    
    def search(self, name):
        l = []
        for key, val in PhoneBook.phoneBook.items():
            if val[0] == name:
                l.append(val)
        
        return "No Data" if not l else l

    def delete(self):
        del PhoneBook.phoneBook[self.id]
    
    def show_phoneBook(self):
        return tuple(val for key, val in PhoneBook.phoneBook.items())

    
ujjawal = PhoneBook("Ujjawal", "1212121212")
ujjawal_patidar = PhoneBook("Ujjawal", "9999999999")
vaibhav = PhoneBook("Vaibhav","9797979797")
aaditya = PhoneBook("Aaditya", "2222222222")

print("Search \"Ujjawal\"")
print(aaditya.search("Ujjawal"))
print()

print("ujjawal_patidar deleted")
ujjawal_patidar.delete()
print()

print("Show phoneBook")
print(vaibhav.show_phoneBook())
print()

print("Search \"Ujjawal\"")
print(aaditya.search("Ujjawal"))
print()


print("Delete Aaditya")
aaditya.delete()

print(vaibhav.show_phoneBook())
print()

print("Update vaibhav phone_number")
vaibhav.update("0000000000")

print(vaibhav.show_phoneBook())






