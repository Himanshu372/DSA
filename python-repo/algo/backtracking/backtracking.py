from typing import List

class Solution:
    # Backtracking problem for returning all combinations of k numbers out of 1 ... n.
    # n=4, k=2 => [[1,2],[1,3],[1,4],[2,4],[3,4],[2,3],]
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res
    # res = set()
    # for i in range(1, n + 1, k):
    #     for j in range(i, min(i + k, n + 1)):

    # [1, 2] => [[1, 2], [2, 1]]
    def permute(self, n: List[int]) -> List[List[int]]:
        res = []
        # k = len(n)
        def backtrack(curr_path: List[int], available: List[int]):
            if len(curr_path) == len(n):
                res.append(curr_path[:])
                return
            for i in range(len(available)):
                curr_path.append(available[i])
                new_available = available[:i] + available[i + 1:]
                backtrack(curr_path, new_available)
                # path.append(i)
                # backtrack(i + 1, path)
                # path.pop()
                curr_path.pop()
        backtrack([], n)
        return res

    def parenthesis(self, n: int) -> List[List[str]]:
        res = []
        l = ["("] * 3
        l.extend(")"* 3)
        # k = len(n)
        # def recur(l, m: List[str]):
        #     for i in range(len(l)):
        def recur(curr: List[str], open_count, close_count):
            if len(curr) == 2 * n:
                res.append("".join(curr[:]))
                return
            # for i in range(len(l)):
            if open_count < n:
                curr.append("(")
                recur(curr, open_count + 1, close_count)
                curr.pop()
            if close_count < open_count:
                curr.append(")")
                recur(curr, open_count, close_count + 1)
                curr.pop()
        recur([], 0, 0)
        return res

    def word_exists(self, board: List[List[str]], word: str) -> bool:
        # if board == 0:
        #     return False
        rows, cols = len(board), len(board[0])
        visited = dict()
        def backprop(row: int, col: int, n: int):
            if n == len(word):
                return True
            
            if (row < 0 or row >= rows 
                or col < 0 or col >= cols
                or visited.get((row, col)) 
                or board[row][col] != word[n]):
                return False
            
            visited[(row, col)] = True
            
            directions = [
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1)
            ]
            for x, y in directions:
                if backprop(row + x, col + y, n + 1):
                    return True

            visited[(row, col)] = False
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backprop(r, c, 0):
                    return True
        return False
