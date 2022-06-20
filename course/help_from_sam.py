from numpy import source


def solve(A):
    if A <= 1:
        return A
    if A == 2:
        return 1

    score1 = 0
    target = 0
    count = 0
    if A % 2 != 0 :
        count = 1
        score1 = 1
        target = A - 1
    else:
        score1 = 2
        target = A - 2

    while score1 * 2 <= target:
        score1 = score1 * 2
    
    return count + target - score1+1

print(solve(4))
print(solve(5))
print(solve(3))
print(solve(7))