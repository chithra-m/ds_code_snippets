def singleNumber(A):
        x = 0
        count = [0]*32

        for i in A:
            for j in range(32):
                if ( i >> j ) & 1:
                    count[j] += 1
        print(count)
        for i in range(32):
            if (count[i] % 3) != 0:
                x = x | (1 << i)

        return x

A = [2,2,2,3,3,3,4]
print(singleNumber(A))


A = [2,2,2,3,3,3,5]

2 = 0 1 0 
2 = 0 1 0
2 = 0 1 0
3 = 0 1 1
3 = 0 1 1
3 = 0 1 1
5 = 1 0 1  

    1  0  1

for i in A:
    for j in range(32):
        if (i >> j) & 1:
