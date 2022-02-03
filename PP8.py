class BinaryTree:
    class _Node:
        def __init__(self, e, left = None, right = None):
            self._left = left
            self._right = right
            self._element = e


    def __init__(self, root = None):
        self._root = root
        self._size = 0

    def is_empty(self):
        return self._root == None

    def add_root(self, e):
        if self._root:
            return None

        self._root = self._Node(e)
        return self._root

    def add_left(self, e, p):
        p._left = self._Node(e)
        return p._left

    def add_right(self, e, p):
        p._right = self._Node(e)
        return p._right

    def _height(self, v):
        if not v:
            return -1
        x = self._height(v._left)
        y = self._height(v._right)
        return 1 + max(x, y)

    def height(self):
        return self._height(self._root)

    def _inOrder(self, p):
        if p:
            self._inOrder(p._left)
            print(p._element)
            self._inOrder(p._right)

    def inOrder(self):
        self._inOrder(self._root)

    def _preOrder(self, p):
        if p:
            print(p._element)
            self._preOrder(p._left)
            self._preOrder(p._right)

    def preOrder(self):
        self._preOrder(self._root)


    def _postOrder(self, p):
        if p:
            self._postOrder(p._left)
            self._postOrder(p._right)
            print(p._element)

    def postOrder(self):
        self._postOrder(self._root)
        
    def copy(self):
        new_root = self._copy(self._root)
        return BinaryTree(new_root)
    
    def _copy(self, p):
        if p == None:
            return None
        new_p = self._Node(p._element)
        new_p._left = self._copy(p._left)
        new_p._right = self._copy(p._right)
        return new_p
    
    def count(self, num):
        num_count = 0
        nums = []
        nums = self._count(self._root, num, num_count, nums)
        for e in nums: #i know this strategy is slightly slower but this was the only way this would work
            if e == num:
                num_count += 1
        return num_count
        
    def _count(self, p, num, num_count, nums):
        if p == None:
            return None
        self._count(p._left, num, num_count, nums)
        self._count(p._right, num, num_count, nums)
        nums.append(p._element)
        return nums
        
    def equal(self, other):
        return self._equal(self._root, other._root)
        
    
    def _equal(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return (p._element == q._element) and self._equal(p._left, q._left) and self._equal(p._right, q._right)
        return False

if __name__ == '__main__':        
    bt = BinaryTree()
    root = bt.add_root(10)
    left_child = bt.add_left(5, root)
    bt.add_right(7, root)
    bt.add_left(8, left_child)
    bt.add_right(2, left_child)
    
    #break to help me read these two different binary trees 
    
    other = BinaryTree()
    root = other.add_root(10)
    left_child = other.add_left(5, root)
    other.add_right(7, root)
    other.add_left(8, left_child)
    other.add_right(2, left_child)
    print(bt.equal(other))
