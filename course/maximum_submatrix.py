import sys
def solve(A):
        for i in range(len(A)):
            for j in range(1,len(A[0])):
                A[i][j] += A[i][j-1]

        for j in range(len(A[0])):
            for i in range(1, len(A)):
                A[i][j] += A[i-1][j]


        max_sum = -sys.maxsize
        for i in range(len(A)):
            for j in range(len(A[0])):
                a1 = i 
                b1 = j 
                a2 = len(A)-1
                b2 = len(A[0])-1
                sum = A[a2][b2] 
                print(sum)
                if b1 > 0:
                    sum -= A[a2][b1-1]
                if a1 > 0:
                    sum -= A[a1-1][b2]
                if a1 > 0 and b1 > 0:
                    sum += A[a1-1][b1-1]
                print(i,j,sum)
                max_sum = max(sum, max_sum)

        return max_sum

A = [[-5, -4, -3],
    [-1,  2,  3],
    [2,  2,  4]]
print(solve(A))