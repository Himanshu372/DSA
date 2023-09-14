from typing import List, Dict
import collections


class GraphNode:

    def __init__(self, val: int):
        self.node = val
        self.adjacent = []


class Graph:

    def __init__(self, nodes: list[GraphNode]):
        self.graph = nodes

    def add_adjacent(self, u: GraphNode, v: GraphNode):
        u.adjacent.append(v)
        return

    def bfs(self, base: GraphNode):
        # Keeping track of visited by map
        visited = dict()
        visited[base] = True
        print(base.node)
        # Keeping track of traversal by list
        traversed = []
        for base_adj in base.adjacent:
            visited[base_adj] = True
            print(base_adj.node)
            traversed.append(base_adj)
        while len(traversed) != 0:
            curr_node = traversed.pop(0)
            for adj in curr_node.adjacent:
                if not visited.get(adj):
                    visited[adj] = True
                    print(adj.node)
                    traversed.append(adj)
        return

    def dfs(self, base: GraphNode):
        traversed = []
        self._dfs(base, dict(), traversed)
        print("\n".join(str(i.node) for i in traversed))

    def _dfs(self, node: GraphNode, visited: Dict[GraphNode, bool], traversed: List[GraphNode]):
        # Keeping track of traversal by list
        visited[node] = True
        traversed.append(node)
        for base_adj in node.adjacent:
            if not visited.get(base_adj):
                self._dfs(base_adj, visited,  traversed)
        return

    def _dfs_ts(self, node: GraphNode, visited: Dict[GraphNode, bool], stack: List[GraphNode]):
        visited[node] = True
        for adj in node.adjacent:
            if not visited.get(adj):
                self._dfs_ts(adj, visited, stack)
        stack.append(node)
        return
    def topological_sort(self, base: GraphNode) -> List[GraphNode]:
        visited, stack = dict(), []
        self._dfs_ts(base, visited, stack)
        for node in self.graph:
            if not visited.get(node):
                stack.append(node)
        return stack[::-1]





if __name__ == "__main__":
    print("====Started====")
    a, b, c, d = GraphNode(2), GraphNode(3), GraphNode(5), GraphNode(7)
    g = Graph([a, b, c, d])
    g.add_adjacent(a, c)
    g.add_adjacent(a, d)
    g.add_adjacent(c, b)
    #g.bfs(a)
    #g.dfs(a)
    sorted_array = g.topological_sort(a)
    print("\n".join(str(i.node) for i in sorted_array))
    print("====Ended====")

