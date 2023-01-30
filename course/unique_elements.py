def solve(A):        
    A.sort()
    print(A)
    count = 0 
    prev = A[0]
    for i in range(1,len(A)):
        prev = A[i-1]        
        if A[i] <= prev:
            count += prev + 1 - A[i]
            A[i] = prev + 1
            prev = A[i]
    return count

A = [4,5,1,2,3,6,7,6,7]
print(solve(A))