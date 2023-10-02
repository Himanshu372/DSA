from json import JSONDecoder
from Algo.Search.search import Search
from Algo.Sort.sort import Sort
from Data_Structures.Stack.stack import Stack
from Data_Structures.Trees.balanced_trees import BalancedBinaryTree, BinaryTree
from Data_Structures.Queues.queues import Queue
from Data_Structures.Heap.heap import Heap



class FileItem:
    def __init__(self, fname):
        self.fname = fname
    def __repr__(self):
        return self.fname


def from_json(json_object):
    if 'fname' in json_object:
        return FileItem(json_object['fname'])


if __name__ == "__main__":
    print("~~~~ START ~~~~~")
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
    t.preorder_traversal()
    t.postorder_traversal()
    t.inorder_traversal()
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
