def diffPossible(A, B):
    frequency = {}
    # for i in range(len(A)):
    #     for j in range(i+1, len(A)):
    #         print(A[i],A[j],A[i]-A[j])
    #         if A[i] - A[j] == B:
    #             print("rgeydeuj",A[i],A[j])


    for i in range(len(A)-1,-1,-1):
        a = A[i] - B
        b = B + A[i]
        # if B == 0 and rem in frequency:
        #     return 1 
        # print(A[i],a,b)
        if a in frequency  or b in frequency :
            # print(A[i],rem)
            return 1
        elif A[i] not in frequency:
            frequency[A[i]] = i
    
    # print(frequency)
    return 0 

# A = [ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ]
# B = 53
# print(diffPossible(A,B))
A = [ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]
B = 97
print(diffPossible(A,B))
A = [ 1, 5, 4, 1, 2 ]
B = 0
print(diffPossible(A,B))
A = [ 80, 87, 75, 11, 57, 31, 88, 48, 15, 77, 44, 22, 82, 41, 52, 52, 99, 40, 84, 21, 30, 100, 61, 48, 96, 64, 73, 79, 84, 95, 14, 48, 80, 90, 26, 97, 33, 88, 25, 84, 85, 57, 44, 91, 64, 16, 39, 30, 18, 17, 84, 54, 54, 50, 24, 13, 100, 80, 69, 22, 96, 12, 68, 65, 40, 47, 70, 48, 53, 10, 39, 61, 56, 11, 46, 18, 94, 49, 59, 31, 30, 16, 64, 90, 90 ]
B = 1
print(diffPossible(A,B))
A = [ 66, 37, 46, 56, 49, 65, 62, 21, 7, 70, 13, 71, 93, 26, 18, 84, 96, 65, 92, 69, 97, 47, 6, 18, 17, 47, 28, 71, 70, 24, 46, 58, 71, 21, 30, 44, 78, 31, 45, 65, 16, 3, 22, 54, 51, 68, 19, 86, 44, 99, 53, 24, 40, 92, 38, 81, 4, 96, 1, 13, 45, 76, 77, 8, 88, 50, 89, 38, 60, 61, 49, 25, 10, 80, 49, 63, 95, 74, 29, 27, 52, 27, 40, 66, 38, 22, 85, 22, 91, 98, 19, 20, 78, 77, 48, 63, 27 ]
B = 31
A = [ 11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13 ]
B = 60
print(diffPossible(A,B))