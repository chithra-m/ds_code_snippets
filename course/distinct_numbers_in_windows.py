def dNums(A,B):
    if B > len(A):
            return []
    ans = []
    frequency = {}
    for i in range(B):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1 
    count = 0
    print(frequency)
    for  values in frequency.values():
        print(values)
        if values >= 1:
            count += 1
    ans.append(count)

    for i in range(B, len(A)):
        if A[i-B] == A[i]:
            count = count
        else:
            frequency[A[i-B]] -= 1
            if A[i] in frequency:
                frequency[A[i]] += 1
            else:
                frequency[A[i]] = 1

            
            if frequency[A[i-B]] == 0:
                count -= 1
            if frequency[A[i]] == 1:
                count += 1
        ans.append(count)

    
    return ans

A = [1, 2, 1, 3, 4, 3]
B = 3
print(dNums(A,B))