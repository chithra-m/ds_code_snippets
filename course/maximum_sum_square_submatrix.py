
def sum(A, top_left, bottom_right):

    #row prefix 
    for i in range(len(A)):
        for j in range(1, len(A)):
            A[i][j] += A[i][j-1]
    print(A)

    #column prefix 
    for j in range(len(A)):
        for i in range(1,len(A)):
            A[i][j] += A[i-1][j]

    print(A)

    a0 = top_left[0]
    a1 = bottom_right[0]
    b1 = top_left[1]
    b2 = bottom_right[1]

    total = A[a1][b2]

    if b1 > 0:
        total -= A[a1][b1-1]
    if a0 > 0:
        total -= A[a0-1][b2]
    if (a0 > 0 )and (b1 > 0):
        total += A[a0-1][b1-1]

    return total


A = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]

top_left = [0,1]
bottom_right =  [2,3]
print(sum(A, top_left, bottom_right))