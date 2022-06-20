def solve(A):
        total = 0
        j = 1
        while A >= 1:
            if A & 1 == 1:
                total += 5 ** j
            A = A >> 1
            j += 1

        return total

A = 1
# print(5**4+5**2)
print(solve(10))