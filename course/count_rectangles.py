A = [1, 1, 2, 2, 3, 3]
# B = [1, 2, 1, 2, 1, 2]

A = [1, 1, 2, 2]
B = [1, 2, 1, 2]
dictionary = {}
for i in range(len(A)):
    temp = [A[i],B[i]]
    dictionary[str(temp)] = 1

count = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        x1 = A[i]
        y1 = B[i]
        x2 = A[j]
        y2 = B[j]
        if x1 != x2 and y1 != y2:
            if str([x1,y2]) in dictionary and str([x2,y1]) in dictionary:
                count += 1

print(count//2)
