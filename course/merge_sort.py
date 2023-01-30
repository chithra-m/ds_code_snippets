def merge_sort(A, l, r):
    if l == r:
        return 
    mid = (l+r) // 2
    merge_sort(A, l, mid)
    merge_sort(A, mid+1, r)
    return merge(A, l, mid, r)

def merge(A, l, mid, r):
    i = l
    j = mid+1
    temp = []
    while i <= mid and j <= r:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1

    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= r:
        temp.append(A[j])
        j += 1
    print(temp)
    
    return temp

A = [3,7,2,9,1]
merge_sort(A,0,len(A)-1)
print(A)