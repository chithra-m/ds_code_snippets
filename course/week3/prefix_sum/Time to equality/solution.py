class Solution:
    
    def solve(self, A):
        high = max(A)
        count = 0
        for i in A:
            count += high -i
        return count