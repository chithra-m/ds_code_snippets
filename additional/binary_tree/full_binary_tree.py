# To check whether the given is full binary tree or not.
# Full binary tree - for any node ,no. of child is 0 or 2 

class Node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None


def isFullTree(root):
    if root.data == None:
        return True
    elif root.left == None and root.right == None:
        return True
    elif root.left != None and root.right != None:
        return (isFullTree(root.left) and isFullTree(root.right))
    
    return False
            

root = Node(5)
root.left = Node(7)
root.right = Node(10)

print(isFullTree(root))
root.left.left = Node(11)
print(isFullTree(root))
