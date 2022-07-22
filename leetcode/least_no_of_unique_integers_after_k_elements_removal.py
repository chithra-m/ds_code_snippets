def solve(A,B):
    frequency = {}
    for i in range(len(A)):
        if A[i] in frequency:
            frequency[A[i]] += 1
        else:
            frequency[A[i]] = 1

    frequency = sorted(frequency.items(),key = lambda kv:(kv[1],kv[0]))
    print(frequency)

    for i in range(len(frequency)):
        if frequency[i][1] > B :
            return len(frequency) - i
        elif frequency[i][1] < B :
            B = B - frequency[i][1]
        else :
            return len(frequency) - i - 1
        


A = [5,5,4]
k = 1
A = [4,3,1,1,3,3,2]
B = 3

print(solve(A,k))