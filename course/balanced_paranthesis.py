class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None

    def insert(self,data):
        temp = Node(data)
        if self.top == None:
            self.top = temp
        else:
            temp.next = self.top
            self.top = temp 
    
    def pop(self):
        if self.top != None:
            self.top = self.top.next

    def peek(self):
        if self.top != None:
            return self.top.data



def solve(A):
        stack = Stack()
        for i in range(len(A)):
            if A[i] == '(':
                stack.insert(A[i])
            elif A[i] == ')'and stack.peek() == '(':
                stack.pop()
            elif A[i] == ')'and stack.peek() == ')':
                return 0
        
        print(stack.peek())
        if stack.peek() == None:
            return 1

        return 0

A= '()('
print(solve(A))