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


    def push_after(self, key, new_data):
        new_node = Node(new_data)
        current = self.head
        if self.head.data == key :
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            found = False
            while current:
                if current.data == key:
                    new_node.next = current.next 
                    current.next = new_node
                    found = True
                    break
                current = current.next
            if found == False:
                return("NO SUCH ELEMENT FOUND")

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


    def delete_end(self):
        if self.head == None:
            print('NO ELEMENTS TO DELETE')
        else:
            last = self.head
            prev = self.head
            while last.next != None:
                prev = last
                last = last.next
            prev.next = None


    def delete_front(self):
        if self.head == None:
            print('NO ELEMENTS TO DELETE')
        else:
            first = self.head.next
            self.head = first


    def delete_at(self, position):
        if position == 0:
            first = self.head.next
            self.head = first
        else:
            prev = self.head
            current = self.head
            for _ in range(position):
                prev = current
                current = current.next
            
            prev.next = current.next


    def search(self, key):
        found = False
        current = self.head
        while current:
            if current.data == key:
                found = True
                break
            current = current.next
        
        return found


if __name__ == '__main__':
    list1 = Linked_list()
    first = Node(1)
    list1.head = first
    # list1.head = Node(1)
    second = Node(2)
    third = Node(3)

    list1.head.next = second
    second.next = third
    
    list1.push_end(7)
    list1.push_front(1)
    list1.delete_end()

    list1.delete_front()
    list1.print_list()
    print()
    list1.delete_at(1)
    list1.print_list()
    list1.push_after(3,5)
    list1.print_list()
    print(list1.search(5))
    print(list1.search(7))