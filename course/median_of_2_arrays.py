# A = [1, 4, 5]
# B = [2, 3]
A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]
C = []*(len(A)+len(B))

i,j = 0, 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

while i < len(A):
    C.append(A[i])
    i += 1
        

while j < len(B):
    C.append(B[j])
    j += 1        
print(C)
half = len(C) // 2
print(C[half],C[half+1])
if (len(C) % 2) == 0:
    print((C[half] + C[half-1])/2)
else:
    print(C[half])