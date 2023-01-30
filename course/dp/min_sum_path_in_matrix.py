def min_cost(i, j, dp):
    print(i,j)
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != '*':
        return dp[i][j] 

    if i == 0 and j == 0:
        dp[i][j] = A[i][j]
        return dp[i][j]


    if i == 0:
        dp[i][j] = min_cost(i, j-1, dp) + A[i][j]    
    elif j == 0:
        dp[i][j] = min_cost(i-1, j, dp) + A[i][j]
    else:
        dp[i][j] = min(min_cost(i-1, j, dp) , min_cost(i, j-1, dp)) + A[i][j]
    return dp[i][j]

        # dp = [ ['*'] * (len(A[0])+1) ] * (len(A) + 1)
A = [[1, 3, 2], [4, 3, 1], [5, 6, 1]]
A=[
  [20, 29, 84, 4, 32, 60, 86, 8, 7, 37],
  [77, 69, 85, 83, 81, 78, 22, 45, 43, 63],
  [60, 21, 0, 94, 59, 88, 9, 54, 30, 80],
  [40, 78, 52, 58, 26, 84, 47, 0, 24, 60],
  [40, 17, 69, 5, 38, 5, 75, 59, 35, 26],
  [64, 41, 85, 22, 44, 25, 3, 63, 33, 13],
  [2, 21, 39, 51, 75, 70, 76, 57, 56, 22],
  [31, 45, 47, 100, 65, 10, 94, 96, 81, 14]
]
dp = [['*'] * len(A[0]) for i in range(len(A))]
print(min_cost(len(A)-1, len(A)-1, dp)) 
print(dp)