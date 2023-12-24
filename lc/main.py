import sys
from typing import List, Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
    
class Value:
    def __init__(self, val=0):
        self.max_val = val

class Solution:
    def create_tree(self, l: List[int]) -> TreeNode:
        if len(l) == 0:
            return None
        root = l[0]
        t = TreeNode(root)
        q = deque()
        q.append(t)
        l = l[1:]
        while l:
            node = q.popleft()
            if len(l) == 1:
                node.left = TreeNode(l[0])
                q.append(node.left)
                l = l[1:]
            if len(l) >= 2:
                node.left = TreeNode(l[0])
                node.right = TreeNode(l[1])
                q.append(node.left)
                q.append(node.right)
                l = l[2:]
        return t

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        value = Value(-1001)
        self.find_sum(root, value)
        return value.max_val

    def find_sum(self, root: Optional[TreeNode], value: Optional[Value]) -> int:
        if root is None:
            return 0
        left_max = self.find_sum(root.left, value)
        right_max = self.find_sum(root.right, value)
        value.max_val = max(value.max_val, (left_max + right_max) + root.val)
        return max(left_max, right_max) + root.val
    


if __name__== "__main__":
    s = Solution()
    l = [-10,9,20,None,None,15,7]
    tree = s.create_tree(l)
    max_path_sum = s.maxPathSum(tree)
    