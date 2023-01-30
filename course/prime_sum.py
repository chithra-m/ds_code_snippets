import math
def sieve_all_prime(n):
    sieve = [True]*(n+1)
    sieve[0]= False
    sieve[1] = False
    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i] == True:
            for j in range(i*i, n+1, +i):
                if sieve[j] == True:
                    sieve[j] = False 

    return sieve


def primesum(A):
    prime = sieve_all_prime(A)
    print(prime)
    for i in range(2,A):
        print(i,prime[i])
        if prime[i]:
            a = i
            b = A - a 
            if prime[b]:
                return [a,b]


print(primesum(10))