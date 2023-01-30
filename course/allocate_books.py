def books(A, B):
    if B > len(A):
        return -1
    l = max(A)
    r = sum(A)
    ans = -1
    
    while l <= r:
        mid = l + ((r-l)//2)
        if check_no_of_students(A, mid, B):
            ans = mid
            r = mid - 1
        else:
            print("fh")
            l = mid + 1
        
    return ans


def check_no_of_students(A, diff,B):
    count = 1
    sum = 0
    for i in range(len(A)):
        if sum + A[i] <= diff:
            sum += A[i]
        else:
            count += 1
            sum = A[i]
    # if count > B:
    #     return False

    return count <= B

A = [12, 34, 67, 90]
B = 4
print(books(A,B))