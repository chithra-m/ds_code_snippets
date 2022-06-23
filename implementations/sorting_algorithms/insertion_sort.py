def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1,-1,-1):
            if A[j] > A[i]:
                A[j], A[i] = A[i], A[j]
                i -= 1
    return A



A = [5,7,2,9,33,56]
A = [5,7,8,22,44,1,0]
print(insertion_sort(A))