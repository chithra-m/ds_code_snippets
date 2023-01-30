def search(A, B):
    POR = -1 #point of rotation
    l = 0
    r = len(A) - 1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] < A[mid-1] and A[mid] < A[mid+1]:
            POR = mid 
            break
        elif A[mid] > A[len(A)-1]:
            l = mid + 1            
        elif A[mid] < A[len(A)-1]:
            r = mid - 1
            
    print("por",POR)
    if B > A[len(A)-1]:
        return binary_search(A, 0, POR-1, B)
    return binary_search(A, POR, len(A)-1, B)


def binary_search(A, l, r, B):
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == B:
            return mid 
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1 
    return -1 

A = [4,5,6,7,1,2,3]
B = 2
A = [ 9, 10, 11, 12, 14, 15, 17, 19, 24, 25, 30, 39, 40, 44, 46, 48, 51, 53, 54, 56, 59, 60, 69, 70, 73, 75, 80, 87, 88, 89, 92, 93, 97, 99, 104, 107, 109, 110, 111, 117, 123, 124, 125, 126, 127, 128, 135, 136, 137, 141, 148, 153, 154, 161, 166, 167, 169, 175, 177, 180, 181, 182, 185, 186, 189, 193, 198, 202, 1, 2, 6, 7 ]
B = 198
print(search(A,B))