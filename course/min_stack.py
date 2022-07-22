import sys
class MinStack:
    # @param x, an integer
    # @return an integer

    def __init__(self):
        self.list1 = []
        self.min_list = []
        self.min = sys.maxsize


    def push(self, x):
        self.list1.append(x)
        if int(x) < int(self.min):
            self.min = x 
        self.min_list.append(self.min)        

    # @return nothing
    def pop(self):
        if len(self.list1) > 0:
            self.list1.pop()
            self.min_list.pop()

    # @return an integer
    def top(self):
        if len(self.list1) > 0 :
            return self.list1[len(self.list1)-1]        
        else:
            return '-1'

    # @return an integer
    def getMin(self):
        if len(self.min_list) > 0: 
            val = len(self.min_list)-1
            # print(self.list1[val])
            return self.min_list[val]
        else:
            return '-1'

# A = input().split()
# n = A[0]
# i = 1
# stack = MinStack()
# while i < len(A):
#     if A[i] == 'P': #push
#         stack.push(A[i+1])
#         i += 1                 
#     elif A[i] == 'p':
#         stack.pop()
#         # stack_min.pop()
#     elif A[i] == 't':
#         print(stack.top(),end = ' ')
#     elif A[i] == 'g':
#         print(stack.getMin(), end = ' ')
#     i += 1

B = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
C = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
for i in range(len(B)):
    print(B[i], C[i])
print(sys.maxsize)
s='Abracadabra'
print(s.split('a',maxsplit=2))