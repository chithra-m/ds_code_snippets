# def solve(A):
#         temp = [1]
#         while temp[-1] <= A:
#             temp.append(temp[-1]*5)
#         print(temp)
#         ans = 0
#         while A > 0:
#             coins = binary_search(temp, A)
#             print(A, "jhf", coins)
#             ans += 1
#             A = A - coins
#         return ans

# def binary_search(temp, A):
#     l = 0
#     r = len(temp) - 1
#     ans = -1
#     while l <= r:
#         mid = (l+r) // 2
#         if temp[mid] == A:
#             return A 
#         elif temp[mid] < A:
#             ans = mid 
#             l = mid + 1
#         else:
#             r = mid - 1
#         # print(temp[l], temp[r], A)
#     return temp[ans]

# A = 47
# print(solve(A))
import math
print(math.sqrt(23))