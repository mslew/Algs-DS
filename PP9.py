#Author: Max Lewis
#compares sort algorithm times

import time
from matplotlib import pyplot as plt

class Heap:
    def __init__(self):
        self._heap = []

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _last_idx(self):
        return len(self._heap) - 1

    def _left(self, i):
        return i * 2 + 1

    def _right(self, i):
        return i * 2 + 2

    def _parent(self, i):
        return (i - 1) // 2

    def _has_left(self, i):
        return self._left(i) < len(self._heap)

    def _has_right(self, i):
        return self._right(i) < len(self._heap)
    
    def empty(self):
        return len(self._heap) == 0

    def add(self, key):
        self._heap.append(key)
        j = self._last_idx()
        while j > 0 and self._heap[j] < self._heap[self._parent(j)]:
            self._swap(j, self._parent(j))
            j = self._parent(j)


    def remove_min(self):
        if self.empty():
            raise Exception()
        self._swap(0, self._last_idx())
        result = self._heap[-1]
        self._heap.pop()
        # push new element down the heap
        j = 0
        while True:
            min = j
            if self._has_left(j) and self._heap[self._left(j)] < self._heap[min]:
                min = self._left(j)
            if self._has_right(j) and self._heap[self._right(j)] < self._heap[min]:
                min = self._right(j)
            if min == j:
                #found right location for min, break
                break
            self._swap(j, min)
            j = min
        return result

def heap_sort(l):
    heap = Heap()
    #phase I: nlogn
    for e in l:
        heap.add(e)
    sorted_list = []
    #phase II: nlogn
    while not heap.empty():
        sorted_list.append(heap.remove_min())
    return sorted_list

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while j >=0 and key < l[j] :
                l[j+1] = l[j]
                j -= 1
        l[j+1] = key
    return l

def heap_sort_timing(number_of_elements_heap_sort, times_heap_sort, elements):
    number_of_elements_heap_sort.append(float(elements))
    l = list(range(0, elements))
    t1 = time.time()
    heap_sort(l)
    t2 = time.time()
    times_heap_sort.append(float(t2 - t1))
        
def insertion_sort_timing(number_of_elements_insertion_sort, times_insertion_sort, elements):
    number_of_elements_insertion_sort.append(float(elements))
    l = list(range(0, elements))
    t1 = time.time()
    insertion_sort(l)
    t2 = time.time()
    times_insertion_sort.append(float(t2 - t1))
        
def python_sort_timing(number_of_elements_python_sort, times_python_sort, elements):
    number_of_elements_python_sort.append(float(elements))
    l = list(range(0, elements))
    t1 = time.time()
    l.sort()
    t2 = time.time()
    times_python_sort.append(float(t2 - t1))
    
def plot():
    plt.plot(number_of_elements_heap_sort, times_heap_sort, label  = 'Heap Sort')
    plt.plot(number_of_elements_insertion_sort, times_insertion_sort, label = 'Insertion Sort')
    plt.plot(number_of_elements_python_sort, times_python_sort, label = 'Python Sort')
    plt.title('Comparison of Sorting Algorithms')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time to Sort')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    elements = 10000
    number_of_elements_heap_sort = []
    number_of_elements_insertion_sort = []
    number_of_elements_python_sort = []
    times_heap_sort = []
    times_insertion_sort = []
    times_python_sort = []
    while elements != 100000:
        heap_sort_timing(number_of_elements_heap_sort, times_heap_sort, elements)
        insertion_sort_timing(number_of_elements_insertion_sort, times_insertion_sort, elements)
        python_sort_timing(number_of_elements_python_sort, times_python_sort, elements)
        elements += 10000
    plot()