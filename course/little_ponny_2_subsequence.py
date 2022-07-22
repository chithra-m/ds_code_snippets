import sys
def solve(A):
        min_str = ""
        min_len = sys.maxsize
        k = 0
        for i in range(2 ** len(A)):
            temp = ""
            sum = 0
            for j in range(len(A)):
                if (i >> j) & 1:
                    if A[j] < A[len(temp)-1]:
                        temp += A[j]
            print(temp)
            if len(temp) < min_len:
                min_len = len(temp)
                min_str = temp 
        
        return min_str

A = "abcdsfhjagj" 
A = "ksdjgha" 
print(solve(A))