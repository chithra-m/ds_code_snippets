def solve(A, B):
    A.sort()
    i = 0
    j = len(A) - 1 
    count = 0
    while i < j:
        if (A[i] + A[j]) == B:
            print(A[i],A[j],i,j)
            target = A[i]
            i += 1
            temp1 = 1
            while i > 0 and i < j and A[i] == target:
                # print(i)
                temp1 += 1
                i += 1
            j -= 1
            temp2 = 1
            
            while  i < j and j < len(A)-1 and A[j] == A[j+1]:
                # print("here")
                temp2 += 1
                j -= 1
            print(A[i],A[j],temp1,temp2,i,j)
            count += temp1*temp2
            
        elif (A[i] + A[j]) < B:
            i += 1
        else:
            j -= 1
    
    return count

A = [ 2, 4, 4, 5, 6, 8, 10 ]
B = 6
A = [ 2, 2, 3, 4, 4, 5, 6, 7, 10 ]
B = 8
print(solve(A,B))