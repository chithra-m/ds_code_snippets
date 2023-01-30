def solve(A, B):
    c = 0
    l = 0
    r = len(A) - 1
    n = len(A)
    # if A[n-1] < A[n-2]:
    #     print("here")
    #     c = n-1 
    
    while l <= r:
        mid = (l+r) // 2
        
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            c = mid
            break 
        elif A[mid] < A[mid+1]:
            l = mid+1
        elif A[mid] <= A[mid-1]:
            r = mid-1
   
    print(c)
    
    print(binary_search(A, c, len(A)-1, B))
    print(binary_search(A, 0, c-1, B))

    if binary_search(A, c, len(A)-1, B) != -1:
        return binary_search(A, c, len(A)-1, B) 
    elif binary_search(A, 0, c-1, B) != -1:
        return binary_search(A, 0, c-1, B)
    return -1


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


A = [ 1, 2, 3, 4, 5, 10, 9, 8, 7, 6 ]
B = 5
A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12

print(solve(A,B))
