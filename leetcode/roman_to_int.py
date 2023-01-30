def solve(s):
    total = 0
    d = {'I': 1, 'V' : 5, 'X' : 10, 'L':50, 'C' : 100, 'D' : 500, 'M' : 1000}
    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            total -= d[s[i]]
        else:
            total += d[s[i]]
        print(s[i], total)
    return total + d[s[-1]]

s = "III"
s = "LVIII"
# s = "MCMXCIV"
# s = "DCXXI"
print(solve(s))