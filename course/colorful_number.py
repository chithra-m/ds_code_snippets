def solve(A):
    dict1 = {}
    temp = []
    while A > 0:
        temp.append(A%10)
        A = A//10
    print(temp)
    for i in temp:
        prod = 1
        for j in range(32):
            if (i >> j) & 1:
                prod *= temp[j]
        print(prod)
        if prod in dict1:
            return 0
        else:
            dict1[prod] = 1 
    
    return 1

A = 123
print(solve(A))