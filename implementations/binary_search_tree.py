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
    if root.right is None:
        temp = root.right
        if root.left is None:
            root.right = None
        else:
            root = root.left 
            root.left = None
        return temp
    return(root.right)


def delete1(root,data):
    print("root",root.data)
    if root.data == data:
        if root.left is None and root.right is None:
            print("tyy",root.data)
            root = None
            print("tyy",root )
        elif root.left is not None:
            root.data = root.left
            root.left = None
        elif root.right is not None:
            root.data = root.right
            root.right = None
        else: # child = 2
            max = find_max_in_left_sub_tree(root)
            root.data = max
        return "deleted"

    elif root.left is not None:
        if root.left.data <= data:
            return delete(root.left, data)
    
    elif root.right is not None:
        if root.right.data >= data:
            return delete(root.right, data)


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
    
    # elif par.data < cur.data:
    #     if cur.left is None and cur.right is None:
    #         par.right = None
    #     elif cur.left is not None:
    #         par.right = cur.left
    #     elif cur.right is not None:
    #         par.left = cur.right
    #     else:
    #         max = find_max_in_left_sub_tree(cur)
    #         cur.data = max 

    
    elif cur.left is None and cur.right is None:
        if par.data > cur.data:
            par.left = None
        else:
            par.right = None


    elif cur.left is not None:
        if par.data > cur.data:
            par.left = cur.left
        else:
            par.right = cur.left

    elif cur.right is not None:
        if par.data > cur.data:
            par.left = cur.right
        else:
            par.left = cur.right

    else:
            max = find_max_in_left_sub_tree(cur)
            cur.data = max 

    # elif par.data > cur.data:
    #     if cur.left is None and cur.right is None:
    #         par.left = None
    #     elif cur.left is not None:
    #         par.left = cur.left
    #     elif cur.right is not None:
    #         par.left = cur.right
    #     else:
    #         max = find_max_in_left_sub_tree(cur)
    #         cur.data = max 

    # elif par.data < cur.data :
    #     par.left = None


root = Node(10)
insert(root,5)
insert(root,8)
insert(root,12)
insert(root,14)
insert(root,16)
pre_order_traversal(root) 
# print(delete(root,16))
print(delete(root,12))
print("asg")
pre_order_traversal(root)

