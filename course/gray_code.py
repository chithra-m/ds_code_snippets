def to_decimal(s):
    total = 0 
    s= s[::-1]
    for i in range(len(s)):
        if s[i] == '1':
            total += (2 ** i)
    return total

def grayCode(A):
        total = []
        temp = graycode(A, total)
        sol = []
        for i in range(len(temp)):
            sol.append(to_decimal(temp[i]))

        print(sol)

def graycode(A, total):
    
    if A == 1 :
        total.append('0')
        total.append('1')
        return total
    final = []
    temp = graycode(A-1, total)
    # print("temp", temp)
    for i in range(0, len(temp)):
        final.append('0'+ temp[i])

    for i in range(len(temp)-1, -1, -1):
        final.append('1'+temp[i])
    
    return final



A = 2
print(grayCode(A))
print(to_decimal('11010'))