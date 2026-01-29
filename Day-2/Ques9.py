# Implement a program to check if parentheses/brackets in a string are balanced using a stack (list).

st = []
str = input("Enter a string : ")

for i in str:
    if i == '(' or i == '[' or i == '{':
        st.append(i)
    elif i == ')' and st[-1] == '(':
        st.pop()
    elif i == '}' and st[-1] == '{':
        st.pop()
    elif i == ']' and st[-1] == '[':
        st.pop()
    else:
        break

if not st:
    print(True)
else:
    print(False)
        

