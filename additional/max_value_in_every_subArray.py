
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def push(self, new_data):
        while self.size != 0 and self.front.data < new_data:
            self.pop()
        
        new_node = Node(new_data)
    
        if self.rear == None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1


    def is_empty(self):
        return self.front == None and self.rear == None


    def pop(self):
        if self.is_empty():
            return
        else:
            temp = self.front
            self.front = temp.next 

            if self.front == None:
                self.rear = None
        self.size -= 1


    def peek(self):
        if self.front != None:
            return self.front.data
        else:
            return -1


    def print(self):
        if self.is_empty():
            print("NO ELEMENTS FoUND")
        else:
            temp = self.front
            while(temp):
                print(temp.data)
                temp = temp.next


def find_max(A, k):
    q = Queue()
    
    for i in range(0,k+1):
        if q.peek() < A[i] :
            q.push(A[i])
    
    print(q.print())
    left = -k
    right = k
    ans = []

    for i in range(k+1, len(A)):
        print("peek",q.peek())
        ans.append(q.peek())
        right += 1
        left += 1

        if left >= 0 and left < len(A):          
            q.pop()
        
        if right >= 0 and right < len(A):            
            while q.peek() != -1 and (q.peek() <= A[i]):
                q.pop()
            q.push(A[i])
    
    print(ans)
    return ans

A = [6,8,9,2,1,5,3,7,9]
k = 1
print(find_max(A,k))
