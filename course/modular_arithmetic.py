import sys 
sys.setrecursionlimit(1000000)
def solve(A, B):
    factorial = 1
    for i in range(2,B+1):
        factorial *= i
    
    factorial = factorial % ((10**9+(7))-1)
    return pow(A, factorial) % (10**9+(7))


def pow(A, B):
   
    if B == 0:
        return 1 
    elif B == 1 :
        return A % (10**9+(7))

    half = pow(A, B//2)% (10**9+(7))
    if B % 2 == 0:
        return (half * half) % (10**9+(7))
    else:
        return (half * half * (A % (10**9+(7)))) % (10**9+(7))

# B ! = 1*2*3*4*....B
# A = 2
# B = 27
A = 3880
B = 9553

print(solve(A,B))
# print("solution,", 666348826)
print("solution,", 487861130)
