class Queue(object):
    """
    Implementing queue with fixed size and increasing size as and when required
    """
    def __init__(self, size):
        self._front = 0
        self._size = size
        self._array = [None] * self._size

    def __len__(self):
        return len([i for i in self._array if i is not None])

    def __repr__(self):
        lenght = len(self)
        return ' '.join(str(self._array[(self._front + i) % lenght]) for i in range(lenght))


    def enqueue(self, value):
        if self._size == len(self):
            self._resize()
        self._add(value)

    def dequeue(self):
        self._array[self._front] = None
        self._front += 1

    def _resize(self):
        self._size = 2 * self._size
        new_array = [None] * self._size
        counter = self._front
        for i in range(len(self)):
            new_array[i] = self._array[counter % self._size]
            counter += 1
        self._array = new_array
        self._front = 0

    def _add(self, value):
        for i in range(self._front, self._size):
            if self._array[i] is None:
                self._array[i] = value
                return
        else:
            for j in range(0, self._front):
                if self._array[j] is None:
                    self._array[j] = value
                    return



if __name__=="__main__":
    q = Queue(5)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.dequeue()
    q.enqueue(4)
    q.dequeue()
    q.enqueue(0)
    print(q)