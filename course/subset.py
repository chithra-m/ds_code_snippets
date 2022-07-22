def check_bit(n, k):        
    new_num = n >> (k)
    return new_num & 1


def subset(A):
    sol = []
    A.sort()
    for i in range(2**len(A)):
        temp = []
        for j in range(len(A)):
            # if (i >> j) & 1:
            if check_bit(i, j):
                temp.append(A[j])
        sol.append(temp)

    sol.sort()
    return sol


A = [1, 2, 3]

print(subset(A))