class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, new_data):
        if self.data == None:
            self.data = new_data
        else:
            new_node = Node(new_data)
            if new_data < self.data:
                if self.left == None:
                    self.left = new_node
                else:
                    self.left.insert_node(new_data)

            elif new_data > self.data:
                if self.right == None:
                    self.right = new_node
                else:
                    self.right.insert_node(new_data)


    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.data)
        if self.right:
            self.right.in_order_traversal()


    def pre_order_traversal(self):
        print(self.data)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()


    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data)
        
root = Node(5)
root.insert_node(7)
root.insert_node(10)
root.in_order_traversal()
root.post_order_traversal()
root.pre_order_traversal()
