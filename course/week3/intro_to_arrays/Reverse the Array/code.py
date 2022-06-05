class Solution:
    def solve(self, A):
        A = list(A)
        i=0
        j=len(A)-1
        while(i<=j):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            j -=1
        return A