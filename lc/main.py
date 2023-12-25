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
                if node.left is not None:
                    q.append(node.left)
                l = l[1:]
            if len(l) >= 2:
                node.left = TreeNode(l[0])
                node.right = TreeNode(l[1])
                if node.left.val is not None:
                    q.append(node.left)
                if node.right.val is not None:
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
        curr_val = 0 if root.val is None else root.val
        value.max_val = max(value.max_val, left_max + right_max + curr_val, left_max + curr_val, right_max + curr_val, curr_val)
        return max(left_max, right_max) + curr_val
    


if __name__== "__main__":
    s = Solution()
    l1 = [-10,9,20,None,None,15,7]
    l2 = [2,-1]
    l3 = [9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6]
    t1 = s.create_tree(l1)
    t2 = s.create_tree(l2)
    t3 = s.create_tree(l3)
    print(s.maxPathSum(t1))
    print(s.maxPathSum(t2))
    print(s.maxPathSum(t3))
    