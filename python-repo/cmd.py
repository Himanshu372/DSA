from json import JSONDecoder
from Algo.Search.search import Search
from Algo.Sort.sort import Sort
from Data_Structures.Stack.stack import Stack
from Data_Structures.Trees.balanced_trees import BalancedBinaryTree, BinaryTree
from Data_Structures.Queues.queues import Queue
from Data_Structures.Heap.heap import Heap
from typing import List, Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FileItem:

    def __init__(self, fname):
        self.fname = fname

    def __repr__(self):
        return self.fname


def from_json(json_object):
    if 'fname' in json_object:
        return FileItem(json_object['fname'])


def create_tree(l: List[int], q: deque, tree:TreeNode) -> Optional[TreeNode]:
    if not l:
        return None
    # if node is None:
    #     root = l[0]
    #     node = TreeNode(root)
    #     l = l[1:]
    elem = l[0]
    if tree is None:
        tree = TreeNode(elem)
        q = deque([tree])
        return create_tree()
    node = q.popleft()
    node.left = l[1]
    q.append(node.left)
    node.right = l[2]
    q.append(node.right)
    return create_tree(l[3:], q, tree)

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder) == 1 and len(inorder) == 1:
        return TreeNode(preorder[0])
    root = preorder[0]
    pos = inorder.index(root)
    left_subtree, right_subtree = inorder[:pos], inorder[pos:]
    l, r = len(left_subtree), len(right_subtree)
    if l > r:
        if (l - r) % 2 == 0:
            pre = suf = (l - r) / 2
            right_subtree = [None] * pre + right_subtree + [None] * suf
        else:
            suf = (l - r)
            right_subtree = right_subtree + [None] * suf
    else:
        if (r - l) % 2 == 0:
            pre = suf = (r - l) / 2
            left_subtree = [None] * pre + left_subtree + [None] * suf
        else:
            suf = (r - l)
            left_subtree = left_subtree + [None] * suf
    left = create_tree(left_subtree[::-1], deque([]), None)
    return left

    
    node.right = l.popleft()
    return


if __name__ == "__main__":
    print("~~~~ START ~~~~~")
    print(buildTree([3,9,20,15,7], [9,3,15,20,7]))
    f = JSONDecoder(object_hook=from_json)
    obj = f.decode('{"fname": "/foo/bar"}')
    print(obj)
    print("====='Search' problems started=======")
    s = Search([0, 20, 30, 50, 60, 80, 110, 130, 140, 170])
    by_binary = s.binary_search(110)
    by_ternary = s.ternary_serach(110)
    print(f"Index by binary search: {by_binary}")
    print(f"Index by ternary search: {by_ternary}")
    print("====='Search' problems end=======")

    print("======'Sorting' problems started======")
    l = [0, 30, 4, 78, 33, 56, 59, -110, 13, -1, 170]
    sr = Sort(l)
    by_bubble_sort = sr.bubble_sort()
    print(f"Array after sorting by bubble sort {by_bubble_sort}")
    by_insert_sort = sr.insertion_sort()
    print(f"Array after sorting by insertion sort {by_insert_sort}")
    by_merge_sort = sr.merge_sort()
    print(f"Array after sorting by merge sort {by_merge_sort}")
    by_quick_sort = sr.quick_sort()
    print(f"Array after sorting by quick sort {by_merge_sort}")
    print("======='Sorting' problems ended======")
    print("=====Stack started======")
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.pop()
    print(s.top())
    print(s)
    print(s.is_empty())
    print("=====Stack ended======")
    print("=====Binary-tree started======")
    t = BinaryTree(3)
    t.insert(2)
    t.insert(5)
    t.insert(9)
    t.insert(1)
    print("pre-order traversal started")
    print(f"{t.preorder_traversal()}")
    print("post-order traversal started")
    print(f"{t.postorder_traversal()}")
    print("in-order traversal started")
    print(f"{t.inorder_traversal()}")
    t.breath_first_traversal()
    print("=====Binary-tree ended======")
    print("=====Balanced-Binary-tree started======")
    t = BalancedBinaryTree(2)
    t.insert(5)
    t.insert(10)
    t.insert(15)
    t.insert(17)
    print(t)
    print("=====Balanced-Binary-tree ended======")
    t = BalancedBinaryTree(2)
    print("=====Stack ended======")
    print("=====Queue started======")
    q = Queue(5)
    q.enqueue(5)
    q.enqueue(3)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(f"Initial queue {q}")
    q.dequeue()
    q.enqueue(4)
    q.dequeue()
    q.enqueue(0)
    print(f"After dequeue and enqueue {q}")
    print("=====Queue ended======")
    print("=====Heap started=====")
    h = Heap()
    h.insert(5)
    h.insert(10)
    h.insert(15)
    h.insert(7)
    h.delete()
    print(h)
    print("=====Heap ended=====")
    print("~~~~ END ~~~~~")
