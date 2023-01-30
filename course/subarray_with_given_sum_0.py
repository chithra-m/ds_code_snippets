def solve( A):
    temp = {}
    # for i in range(len(A)):
        
    for i in range(1,len(A)):
        # val = A[i] + A[i-1]
        A[i] += A[i-1] 
        # print(val)
        if A[i] in temp or A[i] == 0:
            return 1
        else:
            temp[A[i]] = i 
    return 0

A = [1,2,3,4,5]
print(solve(A))