def solve(A,B,C,D,E):
    #ROW PREFIX
    for i in range(len(A)):            
        for j in range(1,len(A[0])):
            A[i][j] += A[i][j-1]

    #COL PREFIX
    for j in range(len(A[0])):
        for i in range(1,len(A)):
            A[i][j] += A[i-1][j] 

    print(A)
    temp = []
    for i in range(len(B)):
        a1 = B[i] -1
        a2 = D[i]-1
        b1 = C[i]-1
        b2 = E[i]-1
        print(a1,b1,a2,b2)
        sum = A[a2][b2]
        print("rb",sum)
        if a1 > 0:
            sum -= A[a1-1][b2]
            print("rb",sum,A[a1-1][b2])
        if b1 > 0:
            sum -= A[a2][b1-1]
            print("rb",sum,A[a2][b1-1])
        if a1 > 0 and b1 > 0:
            sum += A[a1-1][b1-1]
            print("rb",sum,A[a1-1][b1-1])
        temp.append(sum)
        sum = 0
    return temp

A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]
A = [   [5, 17, 100, 11],
         [0, 0,  2,   8]    ]
B = [1, 1]
C = [1, 4]
D = [2, 2]
E = [2, 4]
print(solve(A,B,C,D,E))