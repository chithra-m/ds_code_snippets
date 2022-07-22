def reverse(s,ans):
    if len(s) == 0:
        return ans
    ans += s[len(s)-1]
    return reverse(s[:len(s)-1],ans)

s = input()
ans = ""
print(reverse(s,ans))
print(ans)