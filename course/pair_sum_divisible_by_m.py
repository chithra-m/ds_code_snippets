def solve(A, B):
    mod = [0]*(B)

    for i in range(len(A)):
        mod[(A[i]%B)] += 1

    for i in range(len(mod)):
        print(i, mod[i])

    i = 1
    j = B-1
    # if B % 2 == 0:
    #     ans = mod[0]
    # else:
    #     ans = mod[0]
    ans = mod[0]-1

    while i < j:
        ans += mod[i] * mod[j]
        i += 1
        j -= 1
    return ans 


A = [ 69, 50, 9, 94, 94, 100, 11, 30, 57, 83, 71, 40, 75, 53, 12, 62, 15, 38, 30, 78, 10, 42, 74, 31, 42, 13, 20, 66, 74, 15, 67, 23, 50, 71, 3, 86, 9, 52, 56, 92, 60, 55, 30, 87, 2 ]
B = 21
print(solve(A,B))