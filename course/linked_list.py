
class Node():
    def __init__(self,value):
        self.value = value
        self.pointer = None


class Linked_List():
    def __init__(self):
        self.head = None 
        

    def insert_node(self,position, value):
        # @param position, an integer
        # @param value, an integer
        temp = Node(value)
        if self.head == None:
            self.head = temp 
        else:
            pos = int(1)
            cur = self.head
            while int(pos) < int(position)-1:
                cur = cur.pointer
                pos += 1
            temp.pointer = cur.pointer
            cur.pointer = temp


    def delete_node(self,position):
        # @param position, integer
        # @return an integer
        if position == 1 :
            self.head = self.head.pointer
        else:
            pos = 1
            cur = self.head
            while int(pos) < int(position)-1 and cur:
                cur = cur.pointer
                pos += 1
            if cur:
                print(cur.value)
                temp = cur.pointer 
                cur.pointer = temp.pointer
            


    def print_ll(self):
        # Output each element followed by a space
        res = []
        if self.head == None:
            return None
        else:
            temp = self.head
            while temp :
                res.append(temp.value)
                temp = temp.pointer
        return res


list1 = Linked_List()
t = int(input())
answer= []
while t > 0:
    inp = input().split()
    
    if inp[0] == 'p':
        list1.print_ll()
    elif inp[0] == 'i':
        list1.insert_node(inp[1],inp[2])
    elif inp[0] == 'd':
        list1.delete_node(inp[1])
    t -= 1