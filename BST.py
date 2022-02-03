class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 


def is_bst(root):
    return is_BST_rec(root)

def is_BST_rec(root):
    if root == None or (root.left == None and root.right == None):
        return True
    if root.left.data >= root.data or root.right.data <= root.data:
        return False 
    elif root.right == None:
        return root.left.data < root.data and is_BST_rec(root.left)
    elif root.left == None:
        return root.right.data >= root.data and is_BST_rec(root.right)
    return is_BST_rec(root.left) and is_BST_rec(root.right)

if __name__ == '__main__':
    root = Node(6)
    root.left = Node(4)
    root.right = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(8)
    print(is_bst(root))