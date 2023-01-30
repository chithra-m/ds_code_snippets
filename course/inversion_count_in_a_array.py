def merge_sort(A, l, r):
    if l >= r:
        return 0
    mid = (l+r) // 2
    left = merge_sort(A, l, mid)
    right = merge_sort(A, mid+1, r)
    return left + right + merge(A, l, mid, r)

def merge(A, left, mid, right):
    i = left
    j = mid+1
    temp = []
    count = 0
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            count += mid -i +1
            temp.append(A[j])
            j += 1
    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= right:
        temp.append(A[j])
        j += 1
        
    for i in range(left, right+1):
        A[i] = temp[i-left]
    return count

A = [3,7,2,9,1]
count = 0
print(merge_sort(A,0,len(A)-1))
# print(A)