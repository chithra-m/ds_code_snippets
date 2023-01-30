def solve(A):
    i = 0
    first = A[i]
    second = A[i+1]
    while i <= len(A)+1:
        if second[0] >= first[1]:
            print("1")
            first = second
            second = A[i+1]
        elif second[0] <= first[1]:
            if second[0] >= first[0] and second[1] > first[1]:
                print("2")
                A[i] = [first[0], second[1]]
                A.pop(i+1)
                i -= 1
                first = A[i]
                second = A[i+1]
            elif second[0] >= first[0] and second[1] <= first[1]:
                print("3",A,first,second)
                A[i] = [first[0], first[1]]
                A.pop(i+1)
                print("after pop",A)
                i -= 1
                first = A[i]
                second = A[i+1]
        i += 1

    return A

A = [[1,4],[2,3],[8,10],[15,18]]
A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
print(solve(A))