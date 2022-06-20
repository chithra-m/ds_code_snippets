def solve(A):
        left = []
        right = []
        total = 0 #total no of 1's
        max_one = 0 #max consecutive 1 subarray size
        
        if A == "01" or A== "10":
            return 1

        if A.find('0') == -1:
            return len(A)

        cur_one = 0

        #left array
        if A[0] == '0':
            left.append(0)
        else:    
            total += 1
            cur_one += 1
            left.append(1)
        
        for i in range(1,len(A)):
            if A[i] == '1': 
                total += 1
                cur_one += 1
                if left[i-1] >= 1:
                    left.append(left[i-1]+1)
                else:
                    left.append(1)
            elif A[i] == '0':
                left.append(0)
                max_one = max(max_one, cur_one)
                cur_one = 0
                
        max_one = max(max_one,cur_one)
        
        #right array
        if A[len(A)-1] == '0':
            right.append(0)
        else:    
            right.append(1)

        for i in range(len(A)-2,-1,-1):
            if A[i] == '1': 
                if right[len(right)-1] >= 1:
                    right.append(right[len(right)-1] + 1)
                else:
                    right.append(1)
            elif A[i] == '0':
                right.append(0)
        
        right.reverse()
        temp = max_one
        for i in range(1,len(A)-1):
            if A[i] == '0':
                temp = left[i-1] + right[i+1]
                if temp < total:
                    temp += 1
                else:
                    temp
            max_one = max(max_one, temp)

        return max_one

A="100001011"
# A="00111011"
A = "01"
# A = "010100110101"
A = "0111111111"
print(solve(A))