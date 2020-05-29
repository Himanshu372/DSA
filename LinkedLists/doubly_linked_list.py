class DLL_Node(object):
    """
    Storage class for doubly linked list
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList(object):
    """
    Implementation class for doubly linked list
    """

    def __init__(self, value=None):
        self.head = DLL_Node(value)

    def __len__(self):
        lenght = 0
        curr_node = self.head
        while curr_node is not None:
            lenght += 1
            curr_node = curr_node.next
        return lenght

    def _get(self, value):
        curr_node = self.head
        if curr_node.value == value:
            return node
        while curr_node.next is not None:
            curr_node = curr_node.next
            if curr_node.value == value:
                return curr_node
        return False

    def insert_end(self, value):
        node = DLL_Node(value)
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        node.previous = curr_node

    def insert_start(self, value):
        node = DLL_Node(value)
        curr_head = self.head
        node.next = curr_head
        curr_head.previous = node
        self.head = node

    def insert_between(self, value):
        node = DLL_Node(value)
        lenght = len(self)
        curr_node = self.head
        counter = 1
        while curr_node.next is not None:
            if counter == lenght // 2:
                next_node = curr_node.next
                curr_node.next = node
                node.previous = curr_node
                node.next = next_node
                next_node.previous = node
                return
            curr_node = curr_node.next
            counter += 1

    def delete(self, value):
        node = self._get(value)
        curr_node = self.head
        if node:
            if curr_node == node:
                next_node = curr_node.next
                next_node.previous = None
                self.head = next_node
                return
            while curr_node.next is not None:
                next_node = curr_node.next
                if next_node == node:
                    next_node = next_node.next
                    curr_node.next = next_node
                    next_node.previous = curr_node
                    return
                curr_node = next_node
        else:
            print('Node not found')

    def display(self):
        curr_node = self.head
        print(curr_node.value)
        while curr_node.next is not None:
            next_node = curr_node.next
            print(next_node.value)
            curr_node = next_node