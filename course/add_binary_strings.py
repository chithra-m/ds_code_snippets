def make_equal_length(A,B):

    if len(A) > len(B):
        for _ in range(0,len(A)-len(B)):
            B = '0' + B
    else:
        for _ in range(0,len(B)-len(A)):
            A = '0' + A

    return [A,B]


def addBinary(A, B):
    final = ""
    A,B = make_equal_length(A,B)
    print(A)
    print(B)
    carry = 0
    
    for i in range(len(A)-1,-1,-1):
        
        sum = 0
        val = 0
        if carry > 0:
            sum += carry
        if A[i] =='0' and B[i] == '0':
            sum += 0
        elif A[i] == '1' and B[i] == '1':
            sum += 2
        elif (A[i] == '0' and B[i] == '1') or (A[i] == '1' and B[i] == '0'):
            sum += 1
        
        val = sum % 2
        carry = sum // 2
        print(A[i],B[i],sum,val,carry)
        print("final",final)
        final += '0' if val == 0 else '1'

    if carry == 1:
        final += '1' 
    final = final[::-1]
    return final



A = "1"
B = "1"
print(addBinary(A,B))