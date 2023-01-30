import math


def sieve(n):
    sieve = [True]*(n+1)
    sieve[0]= False
    sieve[1] = False
    for i in range(2, n):
        if sieve[i] == True:
            for j in range(i*i, n, +i):
                if sieve[j] == True:
                    sieve[j] = False 

    
    for i in range(n+1):
        print(i, sieve[i])
    return sieve

def solve(A):
    is_prime = sieve(A)
    count = 0
    for i in range(2,A+1):
        factors = 0
        temp = []
        for j in range(2, int(math.sqrt(i))+1):
            if (i % j) == 0:
                if (j*j) == i:
                    if is_prime[j]:
                        factors += 1
                        temp.append(j)
                else:
                    if is_prime[j]:
                        factors += 1
                        temp.append(j)
                    if is_prime[i//j]:
                        factors += 1
                        temp.append(i//j)

        
        print(i, factors,temp)
        if factors == 2:
            count += 1
    print("count", count)
    return count

A = 98
print(solve(A))
# print(sieve(A))