#Author: Max Lewis
#This program will take two stacks and do arithmetic operations with them 

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
  
op_stack = ArrayStack()
val_stack = ArrayStack()
  
def operator(op_stack, val_stack):
    results = []
    num_1 = 0
    num_2 = 0
    op = ''
    for i in range(len(op_stack)):
        list_val = ''
        num_1 = val_stack.pop()
        num_2 = val_stack.pop()
        op = op_stack.pop()
        list_val = num_1 + ' '+ op + ' ' + num_2 
        if op == '+':
            list_val = list_val + ' ' + '=' + ' ' + str((float(num_1) + float(num_2)))
            results.append(list_val)
        elif op == '-':
            list_val = list_val + ' ' + '=' + ' ' + str((float(num_1) - float(num_2)))
            results.append(list_val)
    return results 

if __name__ == '__main__':
    expr = ['7 + 8', '7 - 8', '1 + 1', '1 - 1', '2 - 1']
    for operation in expr:
        operation = operation.split(' ')
        val_stack.push(operation[2]) 
        val_stack.push(operation[0])
        op_stack.push(operation[1])
    expr = operator(op_stack, val_stack)
    for sol in expr:
        print(sol)