def solve(A, B):
    ans = 0
    l = 0
    r = len(A) 
    while l <= r:
        mid = (l+r) // 2
        if check_sum(A, mid, B):
            ans = max(ans, mid)
            print("ans",ans)
            l = mid + 1
        else:
            r = mid - 1

    return ans 

def check_sum( A, k, B):
    sum = 0
    print(k)
    for i in range(k):
        sum += A[i]
    print("sum of firts k",k,sum)
    if sum > B:
        return False

    for i in range(k, len(A)):
        sum += A[i]
        sum -= A[i-k]
        if sum > B:
            return False
        print(sum,A[i],A[i-k])
    return True

A = [ 1, 2, 3, 4, 5 ]
B = 10
A = [5, 17, 100, 11]
B = 130
print(solve(A,B))