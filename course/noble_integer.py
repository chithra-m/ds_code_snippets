def solve(A):
        A.sort(reverse = True)
        total = 0
        count = 0
        cur_val = A[0]
        
        for i in range(1, len(A)):
            if A[i] == cur_val:
                count += 1
            else:
                cur_val = A[i]
                count = 1
                total = i 
            
            print(A[i],total)
            if total == A[i]:# or total == -A[i]:
                return 1
        return -1

A = [ -4, -2, 0, -1, -6 ]
# A = [1,2,3,3]
# A = [-6,-1,4]
print(solve(A))