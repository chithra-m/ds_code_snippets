import sys

from sqlalchemy import false

def find_min_p(q,A,B):
    min_cost = True
    min_p = sys.maxsize
    p = 0
    while p < q:
        while min_cost == True and p<q :
            if A[p] < A[q]:
                min_p = p
                min_cost = False
                break
            p += 1 
        
        if min_cost == True:
            return -1

        if A[p] < A[q] and B[p] < B[min_p]:
            min_p = p
        p += 1

    if min_p == sys.maxsize:
        return -1
    return min_p


def find_min_r(q,A,B): 
    min_cost = True
    min_r = sys.maxsize
    r = q+1
    while r < len(A):
        while min_cost == True and r < len(A) :
            if A[r] > A[q]:
                min_r = r
                min_cost = False
                break
            r += 1 
        
        if min_cost == True or min_r == sys.maxsize:
            return -1

        if A[r] > A[q] and B[r] < B[min_r]:
            min_r = r
        r += 1

    if min_r == sys.maxsize:
        return -1
    return min_r


def solve(A, B):
    min_sum = sys.maxsize
    
    if len(A) < 3:
        return -1

    for q in range(1,len(A)-1):
        min_p = find_min_p(q,A,B)
        if min_p < 0:
            break

        min_r = find_min_r(q,A,B)
        if min_r < 0:
            break
        
        sum = B[min_p] + B[q] + B[min_r]
        if sum < min_sum:
            min_sum = sum

    if min_sum == sys.maxsize:
        return -1  
    return min_sum
                

# A = [1, 6, 4, 2, 6, 9]
# B = [2, 5, 7, 3, 2, 7]
A = [ 5, 9, 10, 4, 7, 8 ]
B = [ 5, 6, 4, 7, 2, 5 ]
# A = [ 2, 4, 5, 4, 10 ]
# B = [ 40, 30, 20, 10, 40 ]
# A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
# B = [ 10, 13, 11, 14, 15, 12, 13, 13, 18, 13 ]
# A = [ 1, 3, 5 ]
# B = [ 1, 2, 3 ]
print(solve(A,B))