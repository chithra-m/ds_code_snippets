import sys 
sys.setrecursionlimit(1000000)
def merge_sort(A, l, r):
    if l > r:
        return
    if l == r:
        return [A[l]]
    mid = (l + r) // 2
    left = merge_sort(A, l, mid)
    right = merge_sort(A, mid + 1, r)
    print(left,right)
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0 
    ans = []
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]): 
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1 
    
    while i < len(left):
        ans.append(left[i])
        i += 1
    
    while j < len(right):
        ans.append(right[j])
        j += 1 
    
    return ans

def compare(x1, x2):
    return x1 % 10 > x2 % 10

A = [12,55,3,25,6,1,9,123]
print(merge_sort(A,0, len(A)-1))


