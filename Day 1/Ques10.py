# Create a CLI calculator that performs basic arithmetic operations based on user input with input validation.

def calc():
    exp = input("\nEnter the expression \neg. a+b, a-b, a/b, a//b, a**b," +"a%" + "b etc\nAnd enter \'end\' to exit\n>>> ")

    if(exp == 'end'):
        return 'end' 

    operIdx = None

    if '//' in exp:
        operIdx = exp.index('//')
        num1 = int(exp[:operIdx])
        num2 = int(exp[operIdx+2:])
        print(f"{num1} // {num2} = {num1 // num2}")
        return 

    if '**' in exp:
        operIdx = exp.index('**')
        num1 = int(exp[:operIdx])
        num2 = int(exp[operIdx+2:])
        print(f"{num1} ** {num2} = {num1 ** num2}")
        return 

    oper = None

    for i in range(0, len(exp)):
        if exp[i] != ' ' and exp[i].isdigit() == False:
            operIdx = i
            oper = exp[i]
            break


    num1 = int(exp[:operIdx])
    num2 = int(exp[operIdx + 1:])

    if oper == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif oper == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif  oper =='/':
        print(f"{num1} / {num2} = {num1 / num2}")
    elif  oper == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    elif  oper == '+' :
        print(f"{num1} + {num2} = {num1 + num2}")


while(True):
    if calc() == 'end':
        break

