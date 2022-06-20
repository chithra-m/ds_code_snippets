from operator import xor
from pprint import pprint
import math

def solve(A):
        xor_all = 0 
        for i in A:
            xor_all ^= i
        
        print(xor_all)
        # x = int(math.log2(xor_all&-xor_all)+1)
        # xor_all = 4
        x = int(xor_all & (not(xor_all-1)))
        # print(x) #finding the right most set bit in xor of 2 unique elements
        # x = 2 ** abs(x-1)
        # print(x)
        x = math.log2(x)
        print(x)
        a = 0
        b = 0  
        for i in A:
            if x & i:
                a ^= i
            else:
                b ^= i 

        return [a,b]

A = [1,2,1,2,3,4]
A = [ 186, 256, 102, 377, 186, 377 ]
print(solve(A))
print(4&4)