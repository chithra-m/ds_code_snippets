def solve_rank(s):
    A = list(s)
    total = 0
    n = len(s)-1
    factorial = 1
    for i in range(2,len(s)):
        factorial *= i 

    for i in s:
        count = 0
        for j in A:
            if j < i:
                count += 1
        total += count * factorial
        A.remove(i)
        if len(A) > 0:
            factorial = factorial // len(A)
    return total + 1


s = 'yash'
print(solve_rank(s))