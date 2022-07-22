def solve(A, B):
    index = {}
    for i in range(len(B)):
        index[B[i]] = i
    print(index)
    
    s1 = A[0]
    for i in range(1,len(A)):
        s2 = A[i]
        temp = False
        for j in range(min(len(s1),len(s2))):
            print(s2[j],s1[j])
            if index[s2[j]] > index[s1[j]]:
                temp = True
                break
            elif index[s2[j]] < index[s1[j]]:
                return 0
            # else: # both are equal
        if temp == False:
            return 0
        s1 = A[i]
    return 1

A = ["hello", "scaler", "interviewbit"]
B = "adhbcfegskjlponmirqtxwuvzy"
# A = ["fine", "none", "no"]
# B = "qwertyuiopasdfghjklzxcvbnm"
print(solve(A,B))