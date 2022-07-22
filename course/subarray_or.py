
def solve(A):
    frequency = {}
    for i in range(len(A)):
        frequency[A[i]] = (len(A)-i) * (i+1)
    print(frequency)
    total = 0
    sum = 0
    for i in range(len(frequency)):
        temp = frequency[A[i]]
        while temp >= 0:
            total = total | A[i]
            temp -= 1
        print(A[i],total)
        sum += total

    return sum

A = [1,2,3,4,5]
print(solve(A))
print(1|1|1|1|1)