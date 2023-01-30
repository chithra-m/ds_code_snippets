def threeSum(A):
    A.sort()
    print(A)
    ans = []
    for i in range(len(A)-2):
        if i > 0 and A[i] == A[i-1]:
            continue
        b = i + 1
        c = len(A) -1 
        while b < c:
            
            val = A[i] + A[b] + A[c]
            print(A[i],A[b],A[c])
            if val == 0:
                ans.append([A[i],A[b],A[c]])
                b += 1
                while b < c and A[b] == A[b-1]:
                    b +=1
                    
                # c -= 1
            elif val < 0:
                b += 1
            else:
                c -= 1
    return ans


A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print(threeSum(A))

