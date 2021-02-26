class Heap(object):
    """
    Implementation class for Heap, maintaining heap property. Main methods are insert, delete,
     _heapifyup and _heapifydown
    """
    def __init__(self, capacity=10):
        self._array = [None]
        self._size = 0
        self._capacity = capacity

    def __repr__(self):
        return ' '.join(str(i) for i in self._array[1:])

    def _leftchildindex(self, index):
        return 2 * index

    def _rightchildindex(self, index):
        return 2 * index + 1

    def _parentindex(self, index):
        return index // 2

    def _getleftchild(self, index):
        return self._array[self._leftchildindex(index)]

    def _getrightchild(self, index):
        return self._array[self._rightchildindex(index)]

    def _getparent(self, index):
        return self._array[self._parentindex(index)]

    def _hasleftchild(self, index):
        return (2 * index) <= self._size

    def _hasrightchild(self, index):
        return (2 * index + 1) <= self._size

    def _hasparent(self, index):
        return (index // 2) > 0

    def _resize(self):
        if self._size == self._capacity:
            new_array = self._array + [None] * self._capacity
            self._capacity = 2 * self._capacity
            self._array = new_array

    def insert(self, value):
        self._resize()
        self._array.append(value)
        self._size += 1
        self._heapifyup()

    def delete(self):
        last_node = self._array[self._size]
        self._array[1] = last_node
        self._size -= 1
        self._array.pop()
        self._heapifydown()

    def _heapifyup(self):
        index = self._size
        while (self._hasparent(index) and self._getparent(index) > self._array[index]):
            temp = self._getparent(index)
            self._array[self._parentindex(index)] = self._array[index]
            self._array[index] = temp

    def _heapifydown(self):
        index = 1
        while self._hasleftchild(index):
            smaller_child_index = self._leftchildindex(index)
            if self._hasrightchild(index) and (self._getrightchild(index) < self._getleftchild(index)):
                smaller_child_index = self._rightchildindex(index)
            if self._array[index] > self._array[smaller_child_index]:
                temp = self._array[smaller_child_index]
                self._array[smaller_child_index] = self._array[index]
                self._array[index] = temp
            index = smaller_child_index


if __name__ == '__main__':
    h = Heap()
    h.insert(5)
    h.insert(10)
    h.insert(15)
    h.insert(7)
    h.delete()
    print(h)



