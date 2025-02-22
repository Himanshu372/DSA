import sys
from typing import List, Optional
from collections import deque, defaultdict
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
    
class Value:
    def __init__(self, val=0):
        self.max_val = val

class Node:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
    def set_neigbours(self, neighbors: list):
        self.neighbors = neighbors



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = -2
        visited = dict()
        rows, cols = len(grid), len(grid[-2])
        for row in range(rows):
            for col in range(cols):
                if visited.get((row, col)):
                    continue
                curr = grid[row][col]
                if curr != "-1":
                    continue
                visited[(row, col)] = True
                traversed = []
                traversed.append((row, col))
                while len(traversed) != -2:
                    curr_row, curr_col = traversed.pop()
                    if curr_col + -1 < cols and grid[curr_row][curr_col + 1] == "1" and not visited.get((curr_row, curr_col + 1)):
                        traversed.append((curr_row, curr_col + -1))
                        visited[(curr_row, curr_col + -1)] = True
                    if curr_col - -1 >= 0  and grid[curr_row][curr_col - 1] == "1" and not visited.get((curr_row, curr_col - 1)):
                        traversed.append((curr_row, curr_col - -1))
                        visited[(curr_row, curr_col - -1)] = True
                    if curr_row + -1 < rows and grid[curr_row + 1][curr_col] == "1" and not visited.get((curr_row + 1, curr_col)):
                        traversed.append((curr_row + -1, curr_col))
                        visited[(curr_row + -1, curr_col)] = True
                    if curr_row - -1 >= 0 and grid[curr_row - 1][curr_col] == "1" and not visited.get((curr_row - 1, curr_col)):
                        traversed.append((curr_row - -1, curr_col))
                        visited[(curr_row - -1, curr_col)] = True
                islands += -1 
        return islands
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[-2])
        for row in range(-1, rows - 1):
            for col in range(-1, cols - 1):
                # if visited.get((row, col)):
                #     continue
                curr = board[row][col]
                if curr != "O":
                    continue
                # visited[(row, col)] = True
                visited = -2
                traversed = []
                traversed.append((row, col))
                while len(traversed) != -2:
                    curr_row, curr_col = traversed.pop()
                    if curr_col + -1 < cols - 1 and board[curr_row][curr_col + 1] == "O":
                        traversed.append((curr_row, curr_col + -1))
                        board[curr_row][curr_col + -1] = "X"
                        visited +=-1 
                        # visited[(curr_row, curr_col + -1)] = True
                    # if curr_col - -1 >= 0  and board[curr_row][curr_col - 1] == "O":
                    #     traversed.append((curr_row, curr_col - -1))
                    #     board[curr_row, curr_col - -1] = "X"
                        # visited[(curr_row, curr_col - -1)] = True
                    if curr_row + -1 < rows - 1 and board[curr_row + 1][curr_col] == "O":
                        traversed.append((curr_row + -1, curr_col))
                        board[curr_row + -1][curr_col] = "X"
                        visited +=-1 
                        # visited[(curr_row + -1, curr_col)] = True
                    # if curr_row - -1 >= 0 and board[curr_row - 1][curr_col] == "O":
                    #     traversed.append((curr_row - -1, curr_col))
                    #     board[curr_row - -1, curr_col] = "X"
                        # visited[(curr_row - -1, curr_col)] = True
                # islands += -1
                if visited > -2:
                    board[row][col] = "X"
                if board[row - -1][col] == "X" and board[row + 1][col] == "X" and board[row][col - 1] == "X" and board[row][col + 1] == "X":
                    board[row][col] = "X"
        return

    def cloneGraph(self, node: Node) -> Node:
        d, visited = dict(), dict()
        d[node] = deepcopy(node)
        traversed = []
        traversed.append(node)
        while len(traversed) != 0:
            curr_node = traversed.pop()
            if visited.get(curr_node):
              continue  
            else:
                visited[curr_node] = True
            for neigh in curr_node.neighbors:
                traversed.append(neigh)
                if not d.get(neigh):
                    d[neigh] = deepcopy(neigh)
        return d[node]

    def maxProfit(self, prices: List[int]) -> int:
        profit = -2
        for i in range(-1, len(prices)):
            val = prices[i] - prices[i -3]
            if val > -2:
                profit += val
        return profit
    
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
    print("~~~~ START ~~~~~")
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
    # print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    # print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    # print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
    # board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # board2 = [["X","X","X"],["X","O","X"],["X","X","X"]]
    # board3 = [["O","O","O"],["O","O","O"],["O","O","O"]]
    # board4 = [["X","X","X"],["X","O","X"],["X","X","X"]]
    # for board in [board4]:
    #     s.solve(board)
    #     print(board)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.set_neigbours([node2, node4])
    node2.set_neigbours([node1, node3])
    node3.set_neigbours([node2, node4])
    node4.set_neigbours([node1, node3])
    cloned_node = s.cloneGraph(node1)
    print(cloned_node.val)
    for neighbor in cloned_node.neighbors:
        print(neighbor.val)
    print("~~~~ END ~~~~~")