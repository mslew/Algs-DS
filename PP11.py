#Author: Max Lewis
#Adding a search(), insert(), and print_in_order() function to the binary tree class. 

import queue
from collections import deque

class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self, root):
        self._root = self._Node(root)
        self._size = 0

    def __len__(self):
        return self._size

    def height(self):
        return self._height(self._root)

    def _height(self, p):
        if not p:
            return 0
        return 1 + max(self._height(p._left), self._height(p._right))

    def in_order(self):
        for e in self._in_order(self._root):
            yield e

    def _in_order(self, p):
        if p is not None:
            for other in self._in_order(p._left):
                yield other
            yield p._element
            for other in self._in_order(p._right):
                yield other

    def pre_order(self):
        for e in self._pre_order(self._root):
            yield e

    def _pre_order(self, p):
        if p:
            yield p._element
            for other in self._pre_order(p._left):
                yield other
            for other in self._pre_order(p._right):
                yield other

    def post_order(self):
        for e in self._post_order(self._root):
            yield e

    def _post_order(self, p):
        if p:
            for other in self._post_order(p._left):
                yield other
            for other in self._post_order(p._right):
                yield other
            yield p._element

    def breadth_first(self):
        q = queue.Queue()
        q.put(self._root)
        while not q.empty():
            p = q.get()
            print(p._element)
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)

    def insert(self, key):
        return self._insert(key)

    def _insert(self, key):
        p = self._root
        parent = None
        while p:
            parent = p
            if key < p._element:
                p = p._left
            else:
                p = p._right
        if key < parent._element:
            parent._left = self._Node(key)
        else:
            parent._right = self._Node(key)
        return p

    def search(self, key):
        result = self._search(key)
        if result == True:
            return print('The number {} is in this binary tree'.format(key))
        else:
            return print('The number {} is not in this binary tree'.format(key))
    
    def _search(self, key):
        stack = deque()
        p = self._root
        while stack or p:
            if p:
                stack.append(p)
                p = p._left
            else:
                p = stack.pop()
                if p._element == key:
                    return True
                else:
                    p = p._right
        return False

        
    def print_in_order(self):
        return self._print_in_order()

    def _print_in_order(self):  
        stack = deque()
        p = self._root
        while stack or p:
            if p:
                stack.append(p)
                p = p._left
            else:
                p = stack.pop()
                print(p._element)
                p = p._right

if __name__ == '__main__':
    tree = LinkedBinaryTree(10) #modified this a little bit, requires a root to be initiliazed when a tree is created. 
    tree.insert(5)
    tree.insert(15)
    tree.insert(12)
    tree.insert(17)
    tree.insert(3)
    tree.insert(7)
    tree.print_in_order()
    tree.search(5)
    tree.search(11)