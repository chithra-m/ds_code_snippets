
import math
def countMinSquares( A):
    dp = [-1] * (A+1)

    def min_sq(A, dp):
        if A <= 1:
            dp[A] = A
            return dp[A]

        if dp[A] != -1:
            return dp[A]
        
        min_count = 1 << 31     
        for i in range(1, int(math.sqrt(A)) + 1):
            sq = i * i 
            if sq > A:
                break
            min_count = min(min_count, min_sq(A-sq, dp) + 1)
        dp[A] = min_count 
        return dp[A]
    min_sq(A, dp)
    print(A, dp) 
    return min_sq(A, dp)

A = 6
print(countMinSquares(A))
    
