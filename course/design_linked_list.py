class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None 
        
        self.size = 0 

    def insert_at_first(self, value):
        temp = Node(value)
        if self.size == 0:
            self.head = temp 
            
        else:
            temp.next = self.head.next 
            self.head = temp 
        self.size += 1


    def insert_at_last(self,value):
        temp = Node(value)
        if self.size == 0:
            self.head = temp 
        else:
            
            self.tail.next = temp
        self.size += 1


    def insert_at(self,position,value):
        temp = Node(value)

        if position > self.size + 1:
            return 

        if position == self.size:
            self.tail.next = temp
        else:
            cur = self.head
            pos = 0
            while cur :
                print("inner")
                if pos-1  == position-2 :
                    temp.next = cur.next
                    cur.next = temp
                else:
                    cur == cur .next
                    pos += 1
        self.size += 1

    
    def delete(self,position):
        if position > self.size:
            return 
        else:
            cur = self.head
            pos = 0
            while cur :
                if pos == position-1 :
                    cur.next = cur.next.next
                else:
                    cur == cur.next
                    pos += 1
        self.size -= 1


    def print_all(self):
        temp = self.head
        while temp:
            print(temp.val,end='->')
            temp = temp.next 
        print('NULL')

A = [   [0, 1, -1],
        [1, 2, -1],
        [2, 3, 1]   ]

list1 = Linked_list()
for i in range(len(A)):
    print("say")
    if A[i][0] == 0:
        list1.insert_at_first(A[i][1])
        print("hj")

    elif A[i][0] == 1:
        list1.insert_at_last(A[i][1])
        print("m")
        
    # elif A[i][0] == 2:
    #     list1.insert_at(A[i][2],A[i][1])
    #     print("22")
    else:
        list1.delete(A[i][1])

list1.print_all()

