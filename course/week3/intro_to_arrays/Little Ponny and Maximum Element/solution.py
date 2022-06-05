class Solution:
    
    def solve(self, A, B):
        count = 0
        flag = False
        for i in A:
            if i == B:
                flag = True
            if i > B:
                count += 1
        if flag:
            return count 
        return -1