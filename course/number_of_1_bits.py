def numSetBits(A):
    sum = 0
    print(A//2,A%2)

    while(A>0):
        digit = A % 2
        A = A // 2
        if digit == 1:
            sum += 1

    return sum

A = 450676354
A = 28
print(numSetBits(A))