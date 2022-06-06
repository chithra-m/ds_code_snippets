def check_palindrome(x):
    if x < 0 or x== 10:
        return False
    s = str(x)
    if len(s) % 2 == 0:
        for i,j in zip(range(0, len(s)//2), range(len(s)-1, (len(s)//2)-1, -1)):
            if s[i] != s[j]:
                return('false')
        return('true')
    else:
        for i,j in zip(range(0, (len(s)//2)), range(len(s)-1, len(s)//2, -1)):
            if s[i] != s[j]:
                return('false')
        return('true')

x = int(input())
print(check_palindrome(x))