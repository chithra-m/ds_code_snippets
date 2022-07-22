def solve(A,B):
    sum = A[0]
    i = 0
    j = 0
    while j < len(A):
        
        if sum < B:
            j += 1
            if j < len(A):
                sum += A[j]
        
        elif sum > B:
            sum -= A[i]
            i += 1

        elif sum == B:
            print(i,j,A[i:j+1])
            return A[i:j+1]

        print(sum,i,j)
    return -1

A = [1, 2, 3, 4, 5]
B = 5
# A = [5, 10, 20, 100, 105]
# B = 110
# A = [ 1, 1000000000 ]
# B = 1000000000

print(solve(A,B))