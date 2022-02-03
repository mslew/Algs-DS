#Author: Max Lewis
#This prorgam will implement a function that reverses a list of elements by pushing them onto a stack
#in one order, and writing them back to the list in reversed order

import queue

class ArrayStack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise queue.Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise queue.Empty('Stack is empty')
        return self._data.pop()
        
def reverse(l):
    stack = ArrayStack()
    for num in l:
        stack.push(num)
    for i in range(len(l)): 
        l[i] = stack.pop()
    return l 
        
if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    print(reverse(l))