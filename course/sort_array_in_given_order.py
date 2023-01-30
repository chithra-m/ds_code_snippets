def solve(A, B):
    dict_a = {}
    for i in range(len(A)):
        if A[i] in dict_a:
            dict_a[A[i]] += 1
        else:
            dict_a[A[i]] = 1
    
    temp = []
    for i in range(len(B)):
        if B[i] in dict_a:
            count = dict_a[B[i]]
            while count != 0:
                temp.append(B[i])
                count -= 1
            del dict_a[B[i]]
    
    c = sorted(dict_a)
    print(c)
    for keys,value in dict_a.items():
        # count = dict_a[keys]
        while value != 0:
            temp.append(keys)
            count -= 1
        del dict_a[keys]

    return temp

A = [ 12, 7 ,18]
B = [ 7, 1, 6, 17, 2, 19, 10 ]
print(solve(A,B))