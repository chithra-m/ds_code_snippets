def solve(A, B, C):
   fact = factorial(max(A,B)+1)
   print((fact[A] %(C)))
   return ((fact[A] % C) * power(fact[B], C-2, C) * power(fact[A-B], C-2, C) % (C))

def power(a,n, C):
    ans = 1 
    for _ in range(n):
        ans *= a 
    return ans % C 

def factorial(n):
    temp = [1]*(n+1)
    temp[2] = 2
    for i in range(1, n+1):
        temp[i] = i * temp[i-1]
    return temp  

A = 3
B = 2
C = 33
print(solve(A,B,C)) 