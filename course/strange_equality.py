def solve(A):
        x = -1
        y = -1
        for i in range(A-1, -1, -1):
            if i ^ A == i + A:
                x = i 
                break 

        i = A+1
        while i > A:
            if i ^ A == i + A:
                y = i 
                break
            i += 1
        print(x,y,x^y)
        y = A-x
        return (x)^(A+y)


A = 2
print(solve(A))