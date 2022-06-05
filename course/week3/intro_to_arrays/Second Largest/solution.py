class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return -1
        large = 0
        sec_large = 0
        for i in A:
            if i >= sec_large:
                if i >=large:
                    sec_large = large
                    large = i
                else:
                    sec_large = i
        return sec_large