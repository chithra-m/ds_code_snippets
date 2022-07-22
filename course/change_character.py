def solve(A, B):
    # dict1 = {}

    # for i in range(len(A)):
    #     if A[i] in dict1:
    #         dict1[A[i]] += 1
    #     else:
    #         dict1[A[i]] = 1
    
    # res = sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
    # print(res)
    # i = 0 
    # while i < len(res):
    #     print(res[i][1])
    #     if res[i][1] <= B and B > 0:
    #         B -= res[i][1]
    #         # del res[i][1]
    #         # i += 1
    #     else:
    #         break
    #     i += 1

    # return len(res) - i
    arr = [0]*26

    for i in range(len(A)):
        arr[(ord(A[i])-97)] += 1
       
    arr.sort()
    print(arr)
    
    i = 0 
    count = 0
    while i < len(arr):
        if arr[i] <= B and B > 0 and arr[i] != 0:
            B -= arr[i]
            count += 1
        else:
            return len(A)-i
        i += 1
    print(B,count)
    return count + B

A = "abcabbccd"
B = 3
A ="umeaylnlfd"
B = 1
print(solve(A,B))

