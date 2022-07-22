import sys
sys.setrecursionlimit(1000000000)

def sum_of_digits(A,sum1):
    if A <= 0:
        return sum1
    
    sum1 += (A % 10)
    print(A,sum1)
    return sum_of_digits(A//10,sum1)

A = 123
sum1 = 0
print(sum_of_digits(A,sum1))