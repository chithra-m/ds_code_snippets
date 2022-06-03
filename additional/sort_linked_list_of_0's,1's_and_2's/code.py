from itertools import count


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    def push_end(self, new_data):
        temp_node = Node(new_data)

        if self.head == None:
            self.head = temp_node
            return

        last = self.head
        while(last.next != None):
            last = last.next
        last.next = temp_node
        temp_node.next = None


    def push_front(self, new_data):
        temp_node = Node(new_data)
        if self.head == None:
            self.head = temp_node
        else:
            temp_node.next = self.head
            self.head = temp_node


    def print_list(self):
        temp = self.head
        if temp == None:
            print("NO ELEMENTS FOUND") 
            return
            
        while(temp):
            print(temp.data)
            temp = temp.next
        

    def size(self):
        temp = self.head
        if temp == None:
            return 0
        count = 0    
        while(temp):
            temp = temp.next
            count += 1
        return count


    def get_element(self, pos):
        if pos == 0:
            return self.head.data
        elif pos == 1:
            temp = self.head.next
            return temp.data
        else:
            temp = self.head
            i = 0
            while i < pos :
                temp = temp.next
                i += 1
            return temp.data 


    def reverse(self):
        current = self.head
        previous = None
        next_element = current.next
        while current:
            current.next = previous
            previous = current
            current= next_element

            if next_element:
                next_element = next_element.next
        self.head = previous


    def count(self):
        cur = self.head
        count = [0,0,0]
        while cur:
            if cur.data == 0:
                count[0] += 1
            elif cur.data == 1:
                count[1] += 1
            else:
                count[2] += 1
            cur = cur.next
        
        return count


def sort(A):
    list = Linked_list()
    for i in A:
        list.push_end(i)
    
    count = list.count()
    temp = Linked_list()
    k = 0
    for i in count:
        for j in range(i):
            temp.push_end(k)
        k += 1

    temp.print_list()


A = [1,1,2,0,1,2,1,0]
sort(A)