class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        root = Node(data)
    elif data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
        
    return root
    

def pre_order_traversal(root):
    if root:
        pre_order_traversal(root.left)
        print(root.data)
        pre_order_traversal(root.right)


def find_max_in_left_sub_tree(root):
    while root.right:
        root = root.right    
    return root


def find_min_in_left_sub_tree(root):
    while root.left:
        root = root.left    
    return root


def delete(root,data):
    par = None
    cur = root

    while cur and cur.data != data:
        par = cur
        if data < cur.data:
            cur = cur.left
        else:
            cur = cur.right
    
    print(cur.data,par.data)

    if cur is None:
        return root

    # leaf node - no child
    elif cur.left is None and cur.right is None:
        if par.data > cur.data:
            par.left = None
        else:
            par.right = None

    # only left child
    elif cur.left is not None and cur.right is None:
            par.left = cur.left
     
    # only right child
    elif cur.right is not None and cur.left is None:
            par.right = cur.right
       
    # 2 childs    
    else:
        max = find_min_in_left_sub_tree(cur)
        val = max.data
        delete(root,val)
        cur.data = val 


root = Node(10)
insert(root,5)
insert(root,8)
insert(root,12)
insert(root,14)
insert(root,16)
insert(root,11)
print("after insertion")
pre_order_traversal(root) 
# print(delete(root,16))
print(delete(root,12))
# print(delete(root,5))
print("after deletion")
pre_order_traversal(root)

