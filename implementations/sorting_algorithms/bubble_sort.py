# def swap(A,i,j):
#     temp = A[j]
#     A[j] = A[i]
#     A[i] = temp


# def sorted(A):
#     for i in range(len(A)-1):
#         if A[i] > A[i+1]:
#             return False
#     return True


# def bubble_sort(A):
#     while sorted(A) != True:
#         for i in range(len(A)-1):
#             if A[i+1] < A[i]:
#                 swap(A,i,i+1)
#     return A

def bubble_sort(A):
    count = 0
    for i in range(len(A)):
        swapped = False
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j] , A[j+1] = A[j+1], A[j]
                count += 1
                swapped = True
        
        if swapped == False:
            break
    print(count)
    return A


A = [5, 3, 4, 1, 2]
A = [7,0,5,66,99,123,456]
A = [8, 22, 7, 9, 31, 5, 13 ]
print(bubble_sort(A))