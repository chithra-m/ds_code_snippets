def longestConsecutive(A):
    temp_dict = {}
    for i in range(len(A)):
        if A[i] not in temp_dict :
            temp_dict[A[i]] = i
        
    count = 0
    for i in range(len(A)):
        temp = 1
        if A[i]-1 not in temp_dict:
            val = A[i] + 1
            while val <= max(A):
                if val in temp_dict:
                    val += 1
                    temp += 1
                else:
                    break
        count = max(temp, count)
    return count

A = [100,4,200,1,3,2]
A = [ 6, 4, 5, 2, 3 ]
print(longestConsecutive(A))