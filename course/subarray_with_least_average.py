
def solve(A, B):
    sum = 0
    index = 0
    for i in range(B):
        sum += A[i]
        index = 0
    min_avg = sum / B
    print(A[i],sum,min_avg,index)

    for i in range(B, len(A)):
        sum -= A[i-B]
        sum += A[i]
        cur_avg = sum / B
        if cur_avg < min_avg:
            min_avg = cur_avg
            index = i - B + 1
        print(list[0],i,A[i],sum,cur_avg,min_avg,index)

    return index

A = [ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
B = 1
# A = [ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ]
# B = 9
print(solve(A,B))