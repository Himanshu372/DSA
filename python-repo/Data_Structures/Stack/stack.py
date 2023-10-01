
class Stack(object):
    """
    Implementation of Stack class. If follows LIFO(Last In First Out) principle
    """
    def __init__(self):
        self._array = []

    def __len__(self):
        return len(self._array)

    def __repr__(self):
        return ' '.join(str(i) for i in self._array)

    def push(self, value):
        self._array.append(value)

    def pop(self):
        value = self._array.pop()
        return value

    def top(self):
        return self._array[-1]

    def is_empty(self):
        return True if len(self) == 0 else False



if __name__=='__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.pop()
    print(s.top())
    print(s)
    print(s.is_empty())