def binary_search(A, l, r, B, pos):
    if l <= r:
        mid = (l+r) // 2
        print(l,r,mid)
        if A[mid] == B:
            return mid 
        if A[mid] > B:
            pos = mid
            return binary_search(A, l, mid-1, B, pos)
        else:
            return binary_search(A, mid+1, r, B, pos)
    else:
        return pos

A = [1, 3, 5, 6]
B = 2
pos = -1
print(binary_search(A,0,len(A)-1,B, pos))