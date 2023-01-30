def solve( A, B):
    
    A.sort()
    count = 0
    i = 0
    j = 1
    while i < len(A) and j < len(A):
        if (A[j] - A[i]) == B:
            print(A[j],A[i])
            count += 1
            i += 1
            j += 1
        elif (A[j]- A[i]) < B:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    
    return count

A = [1, 5, 3, 4, 2]
B = 3
A = [8, 12, 16, 4, 0, 20]
B = 4
A = [1, 1, 1, 2, 2]
B = 0
print(solve(A,B))