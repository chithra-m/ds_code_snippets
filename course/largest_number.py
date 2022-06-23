def largestNumber(A):
    B = list()
    
    s = ""
    for i in A:
        B.append(str(i))

    B.sort(reverse = True)
    for i in B:
        s += str(i) 
    return s

A = [3, 30, 34, 5, 9]
print(largestNumber(A))