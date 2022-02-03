class BinaryTree:
    class _Node:
        def __init__(self, e, left = None, right = None):
            self._left = left
            self._right = right
            self._element = e


    def __init__(self):
        self._root = None
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
            print(p._elemet)
            self._inOrder(p._right)

    def inOrder(self):
        self._inOrder(self._root)

    def _preOrder(self, p):
        if p:
            print(p._elemet)
            self._preOrder(p._left)
            self._preOrder(p._right)

    def preOrder(self):
        self._preOrder(self._root)


    def _postOrder(self, p):
        if p:
            self._postOrder(p._left)
            self._postOrder(p._right)
            print(p._elemet)

    def postOrder(self):
        self._postOrder(self._root)


bt = BinaryTree()
root = bt.add_root(10)
left_child = bt.add_left(5, root)
bt.add_right(7, root)

bt.add_left(8, left_child)
bt.add_right(2, left_child)

print(bt.height())



