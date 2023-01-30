# A = [1,2,3]
# A = [5,4,2]
# count = 0
# for i in range(1,2**(len(A))):
#     print(i)
#     min_val = 1 << 31
#     max_val = - 1 << 31
#     for j in range(len(A)):
#         if (i >> j) & 1:
#             if A[j] < min_val:
#                 min_val = A[j]
#             if A[j] > max_val:
#                 max_val = A[j]
#     count += max_val - min_val 
#     print(max_val,min_val)
# print(count, "expexted 9")
A = [1,2,3]
A.sort()
mod = 1000000007
n = len(A)
max_sum = 0
min_sum = 0
  
for index in range(n):
    print(A[index], 2**index,(2**(n-1-index)) )
    max_sum += A[index] * (2**index)#((1 << index) % mod)
    min_sum += A[index] * (2**(n-1-index))#((1 << (n - 1 - index)) % mod)

print( (max_sum - min_sum) % mod)
        