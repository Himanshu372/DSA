class Node(object):
    """
    Storage class for singly linked list
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList(object):
    """
    Class inplementating singly linked lists
    """

    def __init__(self, value=None):
        self.head = Node(value)

    def __len__(self):
        length = 0
        curr_node = self.head
        while curr_node is not None:
            length += 1
            curr_node = curr_node.next
        return length

    def _get(self, value):
        curr_node = self.head
        if curr_node.value == value:
            return curr_node
        next_node = curr_node.next
        while next_node is not None:
            if next_node.value == value:
                return next_node
            next_node = next_node.next
        return False

    def insert_end(self, value):
        node = Node(value)
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node

    def insert_start(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_between(self, value):
        node = Node(value)
        length = len(self)
        counter = 1
        curr_node = self.head
        while curr_node.next is not None:
            if counter == length // 2:
                next_node = curr_node.next
                curr_node.next = node
                node.next = next_node
                return
            curr_node = curr_node.next
            counter += 1

    def delete(self, value):
        node = self._get(value)
        if node:
            if self.head == node:
                next_node = self.head.next
                self.head = next_node
                return
            curr_node = self.head
            next_node = curr_node.next
            while next_node != node:
                curr_node = next_node
                next_node = next_node.next
            next_node = next_node.next
            curr_node.next = next_node
            return
        else:
            print('Node not found')

    def display(self):
        curr_node = self.head
        print(curr_node.value)
        while curr_node.next is not None:
            curr_node = curr_node.next
            print(curr_node.value)

    def reverse_linked_list(self):
        curr_node = self.head
        previous = None
        while curr_node.next is not None:
            next_node = curr_node.next
            curr_node.next = previous
            previous = curr_node
            curr_node = next_node
        self.head = previous
        return