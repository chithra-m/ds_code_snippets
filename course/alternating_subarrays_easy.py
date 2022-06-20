def solve(A, B):
    list = []
    size = 2*B + 1
    ans = []
    repeat = False

    for i in range(0, len(A)-size+1):
        k = i+1
        repeat = False
        print(i)
        j = size
        while j > 1 :
            print(A[k-1],A[k])
            if A[k] == A[k-1]:
                repeat = True
            j -= 1    
            k += 1
        if repeat == False:
            ans.append(i+size//2)

    return ans
 

A = [1, 0,1,0,1]
B = 1 
A = [0, 0, 0, 1, 1, 0, 1]
B = 0 
print(solve(A, B))