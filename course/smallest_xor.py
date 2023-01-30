def solve(A, B):
    temp = A
    count = 0 
    for i in range(32):
        if A & (1 << i):
            count += 1 

    print(count)
    if count == B:
        return A 
    elif count < B :
        i = 0 
        while count < B:
            if A & (1<<i):
                i += 1
            else:
                temp = temp | (1<<i)
                i += 1
                count +=1 
            
        return temp
    elif count > B:
        i = 0 
        while count > B:
            if A & (1<<i):
                temp = temp ^ (1<<i)
                count -=1 
            i +=1
        return temp

A = 2
B = 0
print(solve(A,B))