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

    @staticmethod
    def traversal(node=None):
        curr_node = node

    @staticmethod
    def _get_children(node):
        curr_node = node
        children = []
        if curr_node.left:
            children.append(curr_node.left)
        if curr_node.right:
            children.append(curr_node.right)
        return children

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

    # Preorder traversal : root -> left subtree -> right subtree
    def preorder_traversal(self, node=None):
        curr_node = node if node else self.root
        print(curr_node.value, end=' ')
        if curr_node.left:
            self.preorder_traversal(curr_node.left)
        if curr_node.right:
            self.preorder_traversal(curr_node.right)

    # Postorder traversal: left subtree -> right subtree -> root
    def postorder_traversal(self, node=None):
        curr_node = node if node else self.root
        if curr_node.left:
            self.postorder_traversal(curr_node.left)
        if curr_node.right:
            self.postorder_traversal(curr_node.right)
        print(curr_node.value, end=' ')

    # Inorder traversal: left subtree -> root -> right subtree
    def inorder_traversal(self, node=None):
        curr_node = node if node else self.root
        if curr_node.left:
            self.inorder_traversal(curr_node.left)
        print(curr_node.value, end=' ')
        if curr_node.right:
            self.inorder_traversal(curr_node.right)

    def breath_first_traversal(self, node=None):
        curr_node = node if node else self.root
        print(curr_node.value)
        children = self._get_children(curr_node)
        for child in children:
            self.breath_first_traversal(child)