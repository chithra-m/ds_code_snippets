def count_sort(A):
    k = max(A) # to find range 0 to 9
    count = [0]*(k+1)
    
    for i in range(len(A)):
        count[A[i]] += 1

    print(count)

    for i in range(1,len(count)): # prefix count
        count[i] = count[i] + count[i-1]

    print(count)

    sol = [0]*len(A)

    for i in range(len(A)-1, -1, -1):
        count[A[i]] -= 1
        sol[count[A[i]]] = A[i]

    return sol


A = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
# A = ['g','e','e','k','s']
print(count_sort(A))