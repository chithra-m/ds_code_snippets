def solve(A):
    spf = sieve(max(A)+1)
    set1 = set()
    for i in range(len(A)):
        while A[i] > 1:
            # print(i)
            f = spf[A[i]]    
            print(A[i],f)
            if f == spf[f]:        
                set1.add(f)
            while (A[i] % f)==0: 
                A[i] = A[i] // f
            
    return len(set1)


def sieve(n):
    sieve = [0]*(n+1)
    for i in range(len(sieve)):
        sieve[i] = i
    for i in range(2, int(n**0.5)+1):
        if sieve[i] == i:
            for j in range(i*i, n, +i):
                if sieve[j] == j:
                    sieve[j] = i 

    return sieve


A = [1, 2, 3, 4]
A = [ 96, 98, 5, 41, 80 ]
print(solve(A))
# print(sieve(41))