def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = (len(A)) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    res = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            
    res += left[i:]
    res += right[j:]
    return res


A = [5,7,8,22,44,1,0]

print(merge_sort(A))