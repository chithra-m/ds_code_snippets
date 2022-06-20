def gcd(a,b):
     
    # Everything divides 0
    if (b == 0):
         return a
    return gcd(b, a%b)

A = 97
B = 45
print(gcd(A,B))
# print(24%30)
# print(24%24)
print(26 ** 0)