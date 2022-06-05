import sys
class Solution:
    
    def solve(self, A):
        min = sys.maxint
        max = -sys.maxint
        for i in A:
            if (i % 2) == 0 and (i > max):
                max = i
            elif (i % 2) != 0 and (i < min):
                min = i
        return max-min