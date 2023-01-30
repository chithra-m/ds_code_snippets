def solve(A):
    i = 0
    while i < len(A):
        if A[i] >= 1 and A[i] <= len(A):
            if A[i] != i+1 and A[i] < len(A) and A[i] != A[A[i]-1]:
                A[A[i]-1] , A[i]= A[i], A[A[i]-1]
                print(A)
            else:
                i += 1
        else:
            i += 1

    positive = False
    for i in range(len(A)):
        if A[i] > 0:
            positive = True
        if A[i] != i+1:
            return i+1

    if positive == False:
        return 1

    return len(A)+1

A = [1, 2, 0]
# A =[3, 4, -1, 1]
A = [ 2, 3, 1, 2 ]
print(solve(A))