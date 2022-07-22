def solve(A,B):

    count = 1
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i] ^ A[j] == B:
                print(A[i],A[j],count)
                count +=1

    frequency = {}
    for i in range(len(A)):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1

    print(frequency)
    count = 0
    for i in range(len(A)):
        j = abs(B ^ A[i])
        print(A[i],j)
        if j in frequency:    
            print(A[i],j,count)
            count += frequency[A[i]]*frequency[j]
            del frequency[A[i]]
        print(frequency)
    
    return count

# A = [5, 4, 10, 15, 7, 6]
# B = 5
A = [ 17, 18, 8, 13, 15, 7, 11, 5, 4, 9, 12, 6, 10, 14, 16, 3 ]
B = 9
print(17^8)
print(solve(A,B))