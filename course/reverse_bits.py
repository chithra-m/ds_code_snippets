def reverse(A):
    if A == 0:
        return 0
    binary_A = []
    while A > 0:
        digit = A % 2
        A = A // 2
        binary_A.append(digit)

    print(binary_A)
    while len(binary_A) < 32:
        binary_A.append(0)
    print(binary_A)

    sum = 0
    j = 0
    for i in range(31,-1,-1):
        sum += (binary_A[j]* (2**i))
        j += 1
        
    print(2**31)
    return sum


A = int(input())
print(reverse(A))