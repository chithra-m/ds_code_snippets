def arrange(A):
    print(A)
    for i in range(len(A)):
        A[i] *= len(A)
    print(A)
    for i in range(len(A)):
        old = A[i] // len(A)
        new = A[old] // len(A)
        A[i] += new 
    print(A)
    for i in range(len(A)):
        A[i] = A[i] % len(A)

    return A

A = [ 2, 1, 3, 0 ]
print(arrange(A))