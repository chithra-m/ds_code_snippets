def twoSum(A, B):
    frequency = {}
    
    for i in range(len(A)):
        k = B - A[i]

        if k in frequency:
            return [frequency[k]+1, i+1]
        else:
            frequency[k] = i
    
    return []

    # for i in range(len(A)):
    #     if A[i] in frequency:
    #         frequency[A[i]].append(i)
    #     else:
    #         frequency[A[i]] = [i]

    # first_index = len(A)+1
    # second_index = len(A)+1

    # for i in range(len(A)):
    #     a = A[i]
    #     b = B - a
    #     if b in frequency:
    #         if a == b:
    #             # temp = frequency
    #             if len(frequency[A[i]]) > 1:
    #                 index = frequency[b][1]
    #         else:
    #             index = min(frequency[b])   
    #         if index < i:
    #             continue
    #         print(index)
    #         if index < second_index:
    #             first_index = i
    #             second_index = index

    # return [first_index+1, second_index+1]


# def find_least(i, frequency):
#     print("A[i",i)
#     print(frequency[i])
#     temp = frequency[i]
#     print("temp,",temp)
#     # for j in range(len(temp)):
#     #     if i <= j and i!= j  :
#     #         return j
#     return min(temp)



# A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
# B = -3
A = [2,7,5,5]
B = 10

print(twoSum(A,B))