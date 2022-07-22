
def sum_of_digits(A,total):
    if A >= 1:
        total += A % 10
        A = A // 10
        return sum_of_digits(A,total)
    return total


def magic(A):
    ans = sum_of_digits(A,0)
    if ans >= 10:
        sum_of_digits(ans,0)
        return magic(ans)
    if ans == 1:
        return 1
    else:
        return 0

A = 83557
A = 1291
print(magic(A))