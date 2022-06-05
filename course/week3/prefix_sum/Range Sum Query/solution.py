class Solution:
   
    def rangeSum(self, A, B):
        pf = []
        pf.append(A[0])
        for i in range(1,len(A)):
            pf.append(pf[i-1]+A[i])

        list =[]
        for i in range(len(B)):
            start = B[i][0]
            end = B[i][1]
            
            if start == 1:
                list.append(pf[end-1])
            else:
                list.append(pf[end-1] - pf[start-2])
        
        return list