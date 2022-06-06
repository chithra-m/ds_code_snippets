class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def push(self, new_data):
        new_node = Node(new_data)
        if self.rear == None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def is_empty(self):
        if self.front == None:
            return True
        return False


    def pop(self):
        if self.is_empty():
            print("NO ELEMENTS TO REMOVE")
        else:
            self.front = self.front.next


    def print(self):
        if self.is_empty():
            print("NO ELEMENTS FoUND")
        else:
            temp = self.front
            while(temp):
                print(temp.data)
                temp = temp.next


q = Queue()
q.print()
q.print()
q.pop()
q.print()

