def solve(A, B):
    open = False
    minus = False
    stack1 = []
    for i in range(len(A)):
        if A[i] >= 'a' and A[i] <= 'z':
            stack1.append(A[i])
        elif A[i] == '(':
            open = True
            if i > 0 and stack1[-1] == '-':
                minus = True 
        elif A[i] == ')':
            open = False
            minus = False 
        elif A[i] == '-':
            if open == True and minus == True:
                # A[i] = '+'
                stack1.append('+')
            else:
                stack1.append(A[i])
        elif A[i] == '+':
            if open == True and minus == True:
                # A[i] = '-'
                stack1.append('-')
            else:
                stack1.append('+')
    print(stack1)

    open = False
    minus = False
    stack2 = []
    for i in range(len(B)):
        if B[i] >= 'a' and B[i] <= 'z':
            stack2.append(B[i])
        elif B[i] == '(':
            if open == True:
                if i > 0 and stack2[-1] == '-' and minus == False:
                    minus = True 
                else:
                    minus = False 
            else:
                open = True 
                minus = True
        elif B[i] == ')':
            open = False
            minus = False 
        elif B[i] == '-':
            if open == True and minus == True:
                # A[i] = '+'
                stack2.append('+')
            else:
                stack2.append(B[i])
        elif B[i] == '+':
            if open == True and minus == True:
                # A[i] = '-'
                stack2.append('-')
            else:
                stack2.append('+')
    print(stack2)

    for i in range(len(stack1)):
        if stack1[i] != stack2[i]:
            return 0 
    return 1

A = "-(a+b+c)"
B = "-a-b-c"

A = "a-b-(c-d)"
B = "a-b-c-d"
A = "(a+b-c-d+e-f+g+h+i)"
B = "a+b-c-d+e-f+g+h+i"

A = "-(-(-(-a+b)-d+c)-q)"
B = "a-b-d+c+q"
print(solve(A,B))