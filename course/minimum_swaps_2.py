def solve(A):
        count = 0
        i = 0
        while i < len(A):
            if i != A[i]:
                print("i",i,A[i])
                A[A[i]], A[i] = A[i],A[A[i]]
                count += 1
            else:
                i += 1

        return count

A = [1,2,3,4,0]
print(solve(A))