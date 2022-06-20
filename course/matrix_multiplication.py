
def solve(A, B):
    sol = []
    for i in range(len(A)):            
        for j in range(len(B[0])):
            temp = []
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
                
                temp.append(sum)
        sol.append(temp)

    return sol

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(solve(A, B))