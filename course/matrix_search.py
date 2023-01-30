def searchMatrix(A, B):
    
    l = 0
    r = len(A)
    row = -1
    while l <= r:
        mid = (l+r) // 2
        if A[mid][0] <= B:
            row = mid 
            l = mid + 1
        else:
            r = mid - 1 
    print(row)
    for i in range(len(A)):
        print(A[i][0], A[i][-1])

        if A[i][0] <= B and A[i][-1] >= B:
            l = 0 
            r = len(A[0]) - 1
            while l <= r:
                mid = (l+r) // 2
                if A[i][mid] == B:
                    return 1 
                elif A[i][mid] < B:
                    l = mid + 1
                else:
                    r = mid - 1
    return 0

A =[
  [3, 3, 11, 12, 14],
  [16, 17, 30, 34, 35],
  [45, 48, 49, 50, 52],
  [56, 59, 63, 63, 65],
  [67, 71, 72, 73, 79],
  [80, 84, 85, 85, 88],
  [88, 91, 92, 93, 94]
]
B = 94
print(searchMatrix(A,B))