class Solution:
    
    def solve(self, A):
        
        pf_even = []
        pf_even.append(A[0])

        pf_odd = []
        pf_odd.append(0)

        for i in range(1,len(A)):
            if i % 2 == 0:
                pf_even.append(pf_even[i-1]+A[i])
                pf_odd.append(pf_odd[i-1])
            else:
                pf_even.append(pf_even[i-1])
                pf_odd.append(pf_odd[i-1]+A[i])
        
        count = 0
        
        for i in range(len(A)):
            if i == 0:
                even_sum= pf_odd[len(A)-1] 
                odd_sum  = pf_even[len(A)-1] - pf_even[i]
                
            else:
                even_sum = pf_even[i-1] + pf_odd[len(A)-1] - pf_odd[i]
                odd_sum = pf_odd[i-1] + pf_even[len(A)-1] - pf_even[i]
            
            if even_sum == odd_sum:
                count += 1
                
        return count