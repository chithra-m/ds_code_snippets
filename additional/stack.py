# stack using linked list
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    
    def push(self, new_data):
        new_node = Node(new_data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    
    def pop(self):
        if self.top == None:
            print("NO ELEMENTS TO POP")
        else:    
            self.top = self.top.next

    
    def print(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


    def size(self):
        temp = self.top
        count = 0
        if temp :
            count += 1
            temp = temp.next
        return count

    
    def is_empty(self):
        if self.top == None:
            return True
        return False


#push, pop takes O(1) time complexity

s = Stack()
s.print()
s.push(1)
s.push(2)
s.pop()
s.print()

#stack using list

s1 = []
s1.append(1)
s1.append(2)
s1.pop()
print(s1)

