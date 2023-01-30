def solve(A):
    return single(A)

def single(A):
    if A == 1:
        return 1
    if A <= 9:
        return 0 
    sum1 = sum(A)    
    return single(sum1)
    

def sum(A):
    if A == 0:
        return 0
    if A >= 1 :
        return (A %10) + sum(A//10)

print(solve(83557))