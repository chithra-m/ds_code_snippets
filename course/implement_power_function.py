def power(A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1
    half = power(A, B//2 , C) % C 
    if B % 2 == 0:
        return (half * half) % C 
    else:
        return (half * half) % C * (A % C) 

print(power(-1,2,20))
print(-1**2)
print((-1**2)%20)
print(1%20)