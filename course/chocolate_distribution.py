def solve(A, B):
    A.sort()
    min_val = 1 << 31 
    for i in range(B-1):
        print(A[i+B-1], A[i])
        if (A[i+B-1] - A[i]) < min_val:
            min_val = A[i+B-1] - A[i] 
    return min_val

A = [3, 4, 1, 9, 56, 7, 9, 12]
B = 5
print(solve(A,B))