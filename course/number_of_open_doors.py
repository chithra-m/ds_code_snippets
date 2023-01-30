def solve(A):
        state = [1]*(A)
        for i in range(2, A):
            for j in range(i, A+1, +i):
                if state[j-1] == 1:
                    state[j-1] = 0
                else:
                    state[j-1] = 1 
            print(state)
        count = 0
        for i in range(1,A):
            if state[i] == 1:
                count += 1
        return count

A = 10
print(solve(A))