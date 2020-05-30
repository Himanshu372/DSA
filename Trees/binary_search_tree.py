class Node(object):
    """
    ADT for implementing Binary tree
    """
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree(object):
    """
    Implementation class for Binary Tree
    """
    def __init__(self, value=None):
        self.root = Node(value)

    def insert(self, value, node=None):
        curr_node = node if node else self.root
        if curr_node.value == value:
            return
        elif curr_node.value < value:
            if curr_node.right:
                return self.insert(value, curr_node.right)
            else:
                node = Node(value)
                curr_node.right = node
                return
        else:
            if curr_node.left:
                return self.insert(value, curr_node.left)
            else:
                node = Node(value)
                curr_node.left = node
                return

    def search(self, value, node=None):
        curr_node = node if node else self.root
        if curr_node.value == value:
            return True
        elif curr_node.value < value:
            if curr_node.right:
                return self.search(value, curr_node.right)
            return False
        else:
            if curr_node.left:
                return self.search(value, curr_node.left)
            return False

    def preorder_traversal(self, node=None):
        curr_node = node if node else self.root
        print(curr_node.value, end=' ')
        if curr_node.left:
            self.preorder_traversal(curr_node.left)
        if curr_node.right:
            self.preorder_traversal(curr_node.right)

    def postorder_traversal(self, node=None):
        curr_node = node if node else self.root
        if curr_node.left:
            self.postorder_traversal(curr_node.left)
        if curr_node.right:
            self.postorder_traversal(curr_node.right)
        print(curr_node.value, end=' ')


    def inorder_traversal(self, node=None):
        curr_node = node if node else self.root
        if curr_node.left:
            self.inorder_traversal(curr_node.left)
        print(curr_node.value, end=' ')
        if curr_node.right:
            self.inorder_traversal(curr_node.right)



if __name__=='__main__':
    t = BinaryTree(3)
    t.insert(2)
    t.insert(5)
    t.preorder_traversal()
    t.postorder_traversal()
    t.inorder_traversal()



