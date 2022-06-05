class Solution:
   
    def solve(self, A):
        pf = []
        pf.append(A[0])

        for i in range(1,len(A)):
            pf.append(pf[i-1] + A[i])

        for i in range(0,len(A)):
            left_sum = pf[i-1]
            if i == 0:
                right_sum = pf[i]
            else:
                right_sum = pf[len(A)-1] - pf[i]   
           
            if left_sum == right_sum:
                return i
        return -1
