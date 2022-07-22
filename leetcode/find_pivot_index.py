

# def solve(A):
#     pf_sum = []
#     pf_sum.append(A[0])
#     for i in range(1, len(A)):
#         pf_sum.append(A[i]+pf_sum[i-1])

#     for i in range(len(A)):
#         left = pf_sum[i-1]
#         right = pf_sum[len(A)-1]-pf_sum[i]

#         if i == 0:
#             left = 0
#             right = pf_sum[len(A)-1]-A[i]

#         if i == len(A)-1:
#             left = pf_sum[i-1]
#             right = 0

#         print(A[i],left,right)

#         if left == right :
#             return i

#     return -1

def solve(A,B):

    left ,right = 0, sum(A)

    for i in range(len(A)):
        right = right - A[i]

        if left == right:
            return i 
        
        left = left + A[i]
    return -1

A = [1,7,3,6,5,6]
B = 0
print(solve(A,B))

