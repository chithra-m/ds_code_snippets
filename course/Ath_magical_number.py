def solve( A, B, C):
    l = min(B, C)
    r = min(B, C) * A 

    lcm = (B*C // gcd(C,B))
    print(lcm)
    while l <= r:
        mid = (l+r) // 2
        count = (mid // B) + (mid // C) - (mid // lcm)
        if count >= A:
            ans = mid % (10**9+(7))
            r = mid - 1
        else:
            l = mid + 1
    return ans
    

def gcd( a, b):
    if b == 0:
        return a
    return gcd(b , a % b)

# A = 4
# B = 2
# C = 3
A = 19
B = 11
C = 13

print(solve(A,B,C))