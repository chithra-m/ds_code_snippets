class Solution:
    
    def solve(self,A, B):
        if B == 1:
            if A[0] > A[len(A)-1]:
                return A[0]
            else:
                return A[len(A)-1]
        
        prefix_a = prefix(A)    
        suffix_a = suffix(A)
        
        i = B-1 
        j = 0
        sum =0
        max = 0
        while i >= 0 :
            j = B - i -2
            
            if i == B-1 :
                max = prefix_a[i]
            else:
                sum = prefix_a[i] + suffix_a[j]
                if sum > max:
                    max = sum
            
            i -= 1 
        # if j == B-1:
        sum = suffix_a[B-1]
        if sum > max:
            max = sum
            
        return max
        
def prefix(A):
    prefix_a = []
    prefix_a.append(A[0])
    for i in range(1,len(A)):
       prefix_a.append(prefix_a[i-1]+A[i])    
    return prefix_a

def suffix(A):
    suffix_a = []
    suffix_a.append(A[len(A)-1])
    i=len(A)-2
    j=1
    while i >= 0 and j < len(A):
        suffix_a.append(A[i]+suffix_a[j-1])
        j += 1
        i -= 1
 
    return suffix_a    
