# Implement a function that generates a random password with 
# specific requirements (length, uppercase, lowercase, digits, special chars).
import random

def gen_password(**kwargs):
    # print(kwargs)
    if kwargs["length"] != kwargs["uppercase"] + kwargs["lowercase"] + kwargs["digits"] + kwargs["special_chars"]:
        return "Not possible specifications"
    
    password = []
    print(kwargs)
    
    for i in range(kwargs["digits"]):
        password.append(str(random.randint(0,10)))
    
    for i in range(kwargs["lowercase"]):
        password.append(chr(random.randint(97, 122)))

    for i in range(kwargs["uppercase"]):
        password.append(chr(random.randint(65, 91)))

    for i in range(kwargs["special_chars"]):
        password.append(chr(random.randint(33, 47)))

    random.shuffle(password)

    return "".join(password)

password = gen_password(length = 15, uppercase = 8, lowercase = 4, special_chars = 2, digits = 1)
print(password)
    
