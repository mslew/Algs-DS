class ListEmpty(Exception):
    pass

class SinglyList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        self._head = self._tail = None
        self._size = 0
        self._current = None #needed to provide iterator suppor

    def is_empty(self):
        return self._size == 0

    def add_head(self, element):
        if self.is_empty():
            new_node = self._Node(element, None)
            self._head = self._tail = self._current = new_node
        else:
            new_node = self._Node(element, self._head)
            self._head = new_node
        self._size += 1

    def add_tail(self, element):
        if self.is_empty():
            self.add_head(element)
        else:
            new_node = self._Node(element, None)
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
    def find_second_last_node(self):
        end = len(self) - 2
        count = 0
        for e in self:
            if count == end:
                return print(e)
            else:
                count += 1
                continue
    
if __name__ == '__main__':
    l = SinglyList()
    for i in range(10):
        l.add_tail(i)
    l.find_second_last_node()