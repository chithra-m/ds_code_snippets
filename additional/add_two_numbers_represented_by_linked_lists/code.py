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

def make_equal_size(list_1, list_2):
    while list_1.size() != list_2.size():
        if list_1.size() > list_2.size():
            diff = list_1.size() - list_2.size()
            for _ in range(0, diff):
                list_2.push_front(0)
        else:
            diff = list_2.size() - list_1.size()
            for _ in range(0, diff):
                list_1.push_front(0)


def add_two_list(list_1,list_2,list_3):
    carry = 0
    i = list_1.size()-1

    while i >= 0:

        if carry > 0:
            val = list_1.get_element(i) + list_2.get_element(i) + carry
            carry = 0
        else:
            val = list_1.get_element(i) + list_2.get_element(i) 
        if val >= 10:
            carry = val//10
            val = val % 10
            
        temp_node = Node(val)
        list_3.push_end(temp_node.data)
        i -= 1
    if carry > 0:    
        list_3.push_front(carry)
    return list_3

def solve(A,B):
    
    list_1 = Linked_list()
    list_2 = Linked_list()
    list_3 = Linked_list()

    #inserting elements in list
    for i in A:
        list_1.push_end(i)
    for i in B:
        list_2.push_end(i)
    
    make_equal_size(list_1, list_2)

    add_two_list(list_1,list_2,list_3)

    list_3.reverse()
    list_3.print_list()


if __name__ == '__main__':
    # A = list(map(int,input().split('->')))
    # B = list(map(int,input().split('->')))
    A=[1,2,3,9]
    B=[4,5,6]
    solve(A,B) 
    