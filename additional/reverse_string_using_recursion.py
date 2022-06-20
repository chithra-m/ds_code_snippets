def rev(s,ans,n):
    if len(s)!= 0:
        ans += s[n-1]
        n -= 1
        return rev(s[0:n],ans,n)
    return ans

s = "argehh1234"
ans = ""
n = len(s)
ans = ""
print(rev(s,ans,n))


    