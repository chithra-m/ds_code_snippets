def selection_sort(A):
    for i in range(len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[j] < A[min]:
                min = j

        A[i], A[min] = A[min] , A[i]
    
    return A         


A = [5,7,2,9,33,56]
print(selection_sort(A))