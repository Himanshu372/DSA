from .binary_search_tree import Node, BinaryTree


class BalancedNode(Node):

    def __init__(self,value=None, parent=None):
        super(BalancedNode, self).__init__(value)
        self.height = 0
        self.parent = None


class BalancedBinaryTree(BinaryTree):

    def __init__(self, value=None):
        super().__init__(value)
        self.root = BalancedNode(value)
        self.container = []

    def __repr__(self):
        return ' '.join(str(i) for i in self._inorder_traversal())

    def _inorder_traversal(self, node=None):
        curr_node = node if node else self.root
        if curr_node.left:
            self._inorder_traversal(curr_node.left)
        self.container.append(curr_node.value)
        if curr_node.right:
            self._inorder_traversal(curr_node.right)
        return self.container

    def _max_child_height(self, node):
        if node.left and node.right:
            return max(node.left.height, node.right.height)
        if node.left is None and node.right:
            return node.right.height
        if node.left and node.right is None:
            return node.left.height
        else:
            return -1

    def _update_height(self, node):
        while node is not None:
            node.height = self._max_child_height(node) + 1
            node = node.parent

    def _height(self, node):
        if node.left is None:
            left_height = -1
        else:
            left_height = node.left.height

        if node.right is None:
            right_height = -1
        else:
            right_height = node.right.height
        bal = right_height - left_height
        return bal

    def insert(self, value, node=None):
        curr_node = node if node else self.root
        if curr_node.value == value:
            return False
        elif curr_node.value > value:
            if curr_node.left:
                if self.insert(value, curr_node.left):
                    self._check_balance()
            else:
                node = BalancedNode(value, curr_node)
                curr_node.left = node
                node.parent = curr_node
                self._update_height(node)
                return True
        else:
            if curr_node.right:
                if self.insert(value, curr_node.right):
                    self._check_balance()
            else:
                node = BalancedNode(value, curr_node)
                curr_node.right = node
                node.parent = curr_node
                self._update_height(node)
                return True

    def _check_balance(self):
        curr_node = self.root
        bal = self._height(curr_node)
        while bal not in [-1, 0, 1]:
            if bal < -1:
                # Right height is less than left, right rotation
                if self._height(curr_node.left) > 0:
                    self._rotate_left(curr_node.left)
                new_root = self._rotate_right(curr_node)
            else:
                # Left height is less than right, left rotation
                if self._height(curr_node.right) < 0:
                    # Left side of right is heavy, requires right rotation
                    self._rotate_right(curr_node.right)
                new_root = self._rotate_left(curr_node)
            self.root = new_root
            bal = self._height(self.root)

    def _rotate_left(self, node):
        parent = node.parent
        right_node = node.right
        node.right = right_node.left
        right_node.left = node
        node.parent = right_node
        if parent:
            if parent.left == node:
                parent.left = right_node
            else:
                parent.right = right_node
        else:
            right_node.parent = parent
        self._update_height(node)
        return right_node

    def _rotate_right(self, node):
        parent = node.parent
        left_node = node.left
        node.left = left_node.right
        left_node.right = node
        node.parent = left_node
        if parent:
            if parent.left == node:
                parent.left = left_node
            else:
                parent.right = left_node
        else:
            left_node.parent = parent
        self._update_height(node)
        return left_node


if __name__ == '__main__':
    t = BalancedBinaryTree(2)
    t.insert(5)
    t.insert(10)
    t.insert(15)
    t.insert(17)
    print(t)
