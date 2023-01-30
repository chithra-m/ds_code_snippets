import sys
def solve(A):
    # max_sum = -sys.maxsize
    first == False
    for j in range(len(A[0])):
        temp = [0]*len(A)
        for k in range(j,len(A[0])):
            for i in range(len(A)):
                temp[i]+= A[i][k] 
            print(temp)
            temp_sum = 0
            sum1 = 0
            
            for i in range(len(temp)):
                temp_sum += temp[i]
                
                if temp_sum > sum1:
                    sum1 = temp_sum
                elif temp_sum < 0:
                    temp_sum = 0

            if first == False:
                max_sum = sum1
                first = True
            if sum1 > max_sum:
                max_sum = sum1 
    return max_sum

A =[
  [-6,  -21,  27,  19, 19],
  [ 0,   0,    5, -21, 19],
  [18,  -27,  -2, -7,  13],
  [-21, -17, -25, -1,   3],
  [0,    -9,  -6, -16, -5],
  [29,    9,  -25, -7, -25]
]
A =[
  [-24, -2,   8, 24, -14, -12],
  [-24, -18, 18, 13,  8,  12]
]
print(solve(A))