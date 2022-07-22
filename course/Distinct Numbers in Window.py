def dNums(A, B):
    frequency = {}
    sol = []
    for i in range(B):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1

    sol.append(len(frequency))
    print(frequency)

    for i in range(B,len(A)):
        print("i,i",i)
        print("dtyhsr",A[i])
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1
        print(frequency)
        frequency[A[i-B]] -= 1
        if frequency[A[i-B]] == 0:
            del frequency[A[i-B]]
        
        print(frequency)
        sol.append(len(frequency))    
    return sol

# A = [1, 2, 1, 3, 4, 3]
# B = 3
A = [ 2, 7, 7, 81, 81 ]
B = 1
print(dNums(A,B))