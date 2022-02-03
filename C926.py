#This is C-9.26 boyo

from heapmodified import Heap

class Element:
    def __init__(self, v, priority):
        self._value = v
        self._priority = priority
    
    def __lt__(self, other):
        return self._priority < other._priority
    
    def __gt__(self, other):
        return self._priority > other._priority
    
    def __str__(self):
        return '{}'.format(self._value)

class Stack:
    def __init__(self):
        self._priority = 0
        self._heap = Heap()
        
    def push(self, value: int):
        element = Element(v = value, priority = self._priority)
        self._heap.add(element)
    
    def pop(self):
        '''returns the element that has pushed most recently'''
        return self._heap.remove_min()
    
    def _priority(self, priority):
        priority -= 1
        return self._priority 
    
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.pop()) #prints 2
    print(s.pop()) #prints 1