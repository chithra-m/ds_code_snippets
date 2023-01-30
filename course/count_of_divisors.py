import math
def sieve_all_prime(n):
    sieve = [True]*(n+1)
    spf = [0]*(n+1)

    for i in range(n+1):
        spf[i] = i 

    sieve[0]= False
    sieve[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i*i, n+1, +i):
                if spf[j] == j:
                    spf[j] = i
                sieve[j] = False
    print(len(spf))
    return spf


def solve(A):
    spf = sieve_all_prime(1000000)
    for i in range(len(A)):
        total = 1
        x = A[i]
        while x > 1:
            f = spf[x]
            count = 0
            while (x % f) == 0:
                count += 1
                x= (x // f)
            
            total *= (count+1)
        A[i] = total
    return A
   

A = [2,3,4,5]
# A = [72]
print(sieve_all_prime(10))
print(solve(A))