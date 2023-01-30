def pal(A, i, j, dp):
    if i > j:
            return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if A[i] == A[j]:
        if i == j:
            dp[i][j] =  1
        else:
            dp[i][j] =  pal(A, i+1, j-1, dp) + 2
    else:
        dp[i][j] = max(pal(A, i, j-1, dp), pal(A, i+1, j, dp))
    
    return dp[i][j]

A = "bebeeed"
dp = [[-1] * len(A) for i in range(len(A))]
print(pal(A, 0, len(A) - 1, dp))

print(dp)