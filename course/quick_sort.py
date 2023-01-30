def quick_sort( A, l, r):
    if l >= r:
        return 
    idx = rearrange(A, l, r)
    quick_sort(A, l, idx-1)
    quick_sort(A, idx+1, r)

def rearrange(A, l, r):
    i = l+1
    j = r 
    while i <= j:
        if A[i] <= A[l]:
            i += 1 
        elif A[j] >= A[l]:
            j -=1
        else:
            A[i] , A[j] = A[j], A[i]
            i += 1
            j -=1

    A[l], A[i-1] = A[i-1], A[l]
    return i-1

A = [ 2, 4, 1,5, 10,1]
A=[ 1, 4, 10, 2, 1, 5 ]

quick_sort(A, 0, len(A)-1)
print(A)