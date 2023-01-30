def cpFact(A, B):
    max1 = 0
    factors = []
    for i in range(1, int(A**0.5)+1):
        if (A % i ) == 0:
            if (A//i) == i:
                if gcd(B,i) == 1:
                    max1 = max(i, max1)
                    factors.append(i)
            else:
                if gcd(B,i) == 1:
                    max1 = max(i, max1)
                    factors.append(i)
                if gcd(B,(A//i)) == 1:
                    max1 = max((A//i), max1)
                    factors.append((A//i))
                # max1 = max(gcd(B,i), i)
                # max1 = max(gcd(B,(A//i)), (A//i))
                # factors.append(i)
                # factors.append(A//i)
    
    for i in factors:
        print(i, gcd(B,i))

    return max1


def gcd(a,b):
    if b == 0:
        return a 
    return gcd(b, a % b)

print(cpFact(90,47))