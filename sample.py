def power(a,ans,n):
    print(a,n,ans)
    if n < 1: 
        return ans 
    ans = ans * a
    return power(a,ans, n-1)

a = 3
n = 3
ans = 1
print(power(a,ans,n))
print((0**0) % 1)