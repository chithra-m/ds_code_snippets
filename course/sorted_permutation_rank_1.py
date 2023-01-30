import collections

def findRank(A):
    mod = 1000003
    N = len(A)

    if N == 1: return 1

    c = collections.Counter(A)
    print(c)
    def precomputefact():
        getfact = [0] * (N+1)
        getfact[0] = 1
        getfact[1] = 1
        for i in range(2,N+1):
            getfact[i] = i * getfact[i-1]
        return getfact
    getfact = precomputefact()
    print(getfact)

    res = 0
    for i in range(N):
        val1 = ord(A[i])
        count = 0
        for j in range(i+1,N):
            val2 = ord(A[j])
            if val2 < val1:
                count += 1
                
        numerator = count
        multipler = getfact[N-i-1]
        denominator = 1
        for num in c:
            denominator = denominator * getfact[c[num]]
        c[A[i]] -= 1
        
        numerator = numerator *  multipler

        val = (numerator // denominator) % mod
        res += (val) % mod

    return(res+1) % mod

A = 'settLe'
print(findRank(A))