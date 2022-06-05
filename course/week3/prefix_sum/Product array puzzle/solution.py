class Solution:
   
    def solve(self, A):
        ans =[]
        prod = 1
        for i in A:
            prod *= i
        for i in A:
            ans.append(prod//i)
        
        return ans