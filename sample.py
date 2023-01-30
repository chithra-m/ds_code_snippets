
def solve( A, B, C):
    n = len(A)
    dp = [[-1] * (C + 1)] * 2

    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                dp[i % 2][j] = 0 
            elif B[i-1] > j:
                dp[i % 2][j] = dp[(i-1) % 2][j]
            else:
                dp[i % 2][j] = max(dp[(i-1) % 2][j], dp[(i-1) % 2][j - B[i-1]] + A[i-1])

    print(dp)
    return dp[len(A) % 2][C]

A = [6, 10, 12]
B = [10, 20, 30]
C = 50
print(solve(A,B,C))
