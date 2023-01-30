def solve(A):
    stack = []
    for i in range(len(A)):
        if A[i] in ['+','-','*','/']:
            b = stack.pop()
            a = stack.pop()
            if A[i] == '*':
                stack.append(a*b)
            elif A[i] == '+':
                stack.append(a+b)
            elif A[i] == '-':
                stack.append(a-b)
            elif A[i] == '/':
                stack.append(a//b)
        else:
            stack.append(int(A[i]))
        print(stack)
    return stack[0]

A = [ "2", "2", "/" ]
A = [ "4", "13", "5", "/", "+" ]
# print(ord('0'),ord('9'))
print(solve(A))