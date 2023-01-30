def solve(A, B):
    l = 1
    r = A[-1] - A[0]
    ans = 1
    while l <= r:
        mid = l + ((r-l) // 2)
        val = check_no_of_cows_placed(mid, A)
        if val >= B:
            ans = mid 
            l = mid + 1
        else:
            r = mid - 1

    return ans 


def check_no_of_cows_placed(diff, A):
    prev = 0
    count = 1
    for i in range(1,len(A)):
        if (A[i] - A[prev]) >= diff:
            count += 1
            prev = i 
    
    return count

A = [ 1, 2, 3, 4, 5 ]
B = 3
print(solve(A,B))