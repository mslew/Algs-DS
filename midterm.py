#Author: Max Lewis
#This is the midterm.

import queue

class ListEmpty(Exception):
    pass

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

class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self._size = 0

        self._current = None 

    def is_empty(self):
        return self._size == 0

    def add_head(self, e):
        if self.is_empty():
            new_node = self._Node(e, None)
            self._head = self._tail = self._current = new_node
        else:
            new_node = self._Node(e, self._head)
            self._head = new_node

        self._size += 1

    def add_tail(self, e):
        if self.is_empty():
            self.add_head(e)
        else:
            new_node = self._Node(e, None)
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1

    def delete_tail(self):
        if self.is_empty():
            raise ListEmpty()
        p = self._head
        while p._next is not self._tail:
            p = p._next
        self._tail = p
        self._tail._next = None
        self._size -= 1

    def delete_head(self):
        if self.is_empty():
            raise ListEmpty()

        p = self._head
        self._head = p._next
        p._next = None

        self._size -= 1

    def __len__(self):
        return self._size


    def __iter__(self):
        """needed to provide iterator support"""
        return self

    def __next__(self):
        """needed to provide iterator support,
        there are several other cases that needs
        to be handled when delete_head, delete_tail
        are interleaved with iterator, one classical
        way of overcomming this is to lock modification
        while iterator is in progress (e.g.: raise
        concurrent modification exception as in java).
        Handling these cases is beyond scope of this
        simple implementation"""

        if self.is_empty():
            raise StopIteration()

        if self._current == None:
            # as a rough solution, start iterator over
            self._current = self._head
            raise StopIteration()
        e = self._current._element
        self._current = self._current._next
        return e
    
    def find_median(self):
        first = self._head
        second = self._head
        while second._next is not None:
            first = first._next
            second = second._next
            if second._next is None:
                break
            else:
                second = second._next
        return first._element
        

def max_and_min(l):
    min = l[0]
    max = l[0]
    for e in l:
        if e > max:
            max = e
        elif e < min: 
            min = e
        else:
            continue
    return min, max

def is_sorted(l):
    first_val = l[0]
    for e in l:
        if first_val > e:
            return print('Not Sorted')
        else:
            first_val = e
            continue
    return print('This list is sorted')

def duplicates(l): 
    l.sort()
    temp = [] 
    for e in l: 
        if e not in temp: 
            temp.append(e) 
        else: 
            return False
    return True

def fun(l, key, count):
    if len(l) == 1:
        if l[0] == key:
            count += 1
        return count
    elif l[0] == key:
        count += 1
        return fun(l[1:], key, count) 
    else:
        return fun(l[1:], key, count) 
    
def is_valid_epxr(expr):
    stack = ArrayStack()
    expr.split(' ')
    for ch in expr:
        if ch in "((":
            stack.push(ch)
        else:
            if len(stack) == 0 and ch in '(())':
                return print('{} is not valid'.format(expr)) 
            elif ch in "))" and stack.top() in "((":
                stack.pop()
                continue
    if len(stack) >= 1:
        return print('{} is not valid'.format(expr))
    return print('{} is valid'.format(expr)) 


if __name__ == '__main__':
    l = [1,2,3,4,5,45,455,34,52345,23453,52345]
    l2 = [1,2,3,4,5,6,7,3,3,1,1]
    l3 = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,5,65,6,7,8,7,5,4]
    l4 = [1,2,3,4,5,6,7,8,9,10]
    expr_list = ['1 + 10', '(1 + 2)', '(2 * 3) + (4 * 2 + (x - 1))', '(1 + 1) + (2 * x))', '((1 + 5) * x', '((1 + 1))']
    count = 0
    l.sort()
    min, max = max_and_min(l)
    print('The max is: {} The min is: {}'.format(max, min))
    is_sorted(l)
    print(duplicates(l4))
    print(fun(l2, 3, count))
    for expr in expr_list:
        is_valid_epxr(expr)
    sl = SinglyList()
    for i in range(11):
        sl.add_tail(i+1)
    print(sl.find_median())