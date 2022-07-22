def solve(A,B):
    for i in range(len(A)):
        if A[i] == '0':
            A[i] = '0'+'1'
        else:
            A[i] = '1'+'0'
    return A


A = 2
B = 1
s =""
print(solve(str(A),B))