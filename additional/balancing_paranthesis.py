s = input()

stack = []

for i in s:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
    elif i == ')':
        if stack[len(stack)-1] == '(':
            stack.pop()
        else:
            print("NOT BALANCED")
            break
    elif i == ']' :
        if stack[len(stack)-1] == '[':
            stack.pop()
        else:
            print("NOT BALANCED")
            break
    elif i == '}' :
        if stack[len(stack)-1] == '{':
            stack.pop()
        else:
            print("NOT BALANCED")
            break

if len(stack) == 0:
    print("BALANCED")


