def solve(A):
    if len(A) <= 2 :
        if int(A) % 8 == 0:
            return 1
        else:
            return 0

    A = A[len(A)-3:len(A)]
    print(A)
    if int(A) % 8 == 0:
            return 1
    else:
        return 0
    # for i,j in range(len(A)) and range(2,-1):
    #     val += int(int(A[i]) + 10 ** j)

    if val % 8 == 0:
        return 1
    else:
        return 0

print(solve('6408'))
print(solve('64'))
# print(641 % 8)