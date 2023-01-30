from unittest.main import MAIN_EXAMPLES


def solve(A):
    A.sort()
    N = len(A)
    mod= 10**9+(7)
    maximum = 0
    minimum = 0

    for i in range(N//2):    
        maximum += abs(A[N-i-1] - A[i])
    
    for i in range(0,len(A),2):
        minimum += (abs(A[i]-A[i+1]))
    
    return [maximum % mod, minimum % mod]

A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
print(solve(A))