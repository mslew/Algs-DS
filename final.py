#Author: Max Lewis
#This is the final exam 

import math 

class BinaryTree: 
    class _Node: 
        def __init__(self, element, left = None, right = None): 
            self._left = left 
            self._right = right 
            self._element: int = element 
            
    def __init__(self): 
        self._root = None 
        self._size = 0 
        
    def equal(self, other):
        result = self._equal(self._root, other._root)
        return result   
    
    def _equal(self, p, q):
        if p == None:
            return None
        elif p._element != q._element:
            return False
        self._equal(p._left, q._left)
        self._equal(p._left, q._left)
        return True

class ArrayBinaryTree: 
    def __init__(self, vals = []): 
        self._heap = vals
    
    def __getitem__(self, i):
        return self._heap[i]
    
    def __str__(self):
        return '{}'.format(self._heap)
    
    def __len__(self):
        return len(self._heap)
    
    def find_ancestors(self, i: int):
        if i > len(self) - 1:
            return None
        ancestors = []
        ancestor = i
        while ancestor != 0:
            ancestor = math.floor((ancestor - 1) / 2)
            ancestors.append(self[ancestor])
        return ancestors

if __name__ == "__main__":
    arr = [4, 9, 8, 17, 26, 50, 16, 19, 69, 32, 93, 55]
    bt = ArrayBinaryTree(arr)
    print(bt.find_ancestors(5))