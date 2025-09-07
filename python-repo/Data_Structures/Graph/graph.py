from typing import List, Dict
import collections

class GraphNode:
    pass

# GraphNodeNonWeighted represent non-weighted graph in form of adjacent lists
class GraphNodeNonWeighted(GraphNode):
    def __init__(self):
        self.adjacent = []

# GraphNodeWeighted reppresnts weighted graph in form adjaceny lists
class GraphNodeWeighted(GraphNode):

    def __init__(self, val: int):
        self.val = val
        self.adjacent = []


# Graph class represent general graph class
class Graph:

    def __init__(self, nodes: list[GraphNode]):
        self.graph = nodes

    def add_adjacent(self, u: GraphNode, v: GraphNode):
        u.adjacent.append(v)
        return
    
    def print(self):
        if len(self.graph) != 0 and isinstance(self.graph[0], GraphNodeNonWeighted):
                for vertex in self.graph:
                    print(f'node: {", ".join(str(each) for each in range(len(vertex.adjacent)))}')
                return  
        if len(self.graph) != 0 and isinstance(self.graph[0], GraphNodeWeighted):
                for vertex in self.graph:
                    print(f'{vertex.val}: {", ".join(str(each.val) for each in vertex.adjacent)}')
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

    def topological_sort(self) -> List[GraphNode]:
        visited, stack = dict(), []
        for node in self.graph:
            if not visited.get(node):
                self._dfs_ts(node, visited, stack)
        return stack[::-1]





if __name__ == "__main__":
    print("====Started====")
    a, b, c, d = GraphNodeNonWeighted(), GraphNodeNonWeighted(), GraphNodeNonWeighted(), GraphNodeNonWeighted()
    g = Graph([a, b, c, d])
    g.add_adjacent(a, c)
    g.add_adjacent(a, d)
    g.add_adjacent(c, b)
    #g.bfs(a)
    #g.dfs(a)
    print(f'printing non weighted graph: {g.print()}')
    sorted_array = g.topological_sort()
    # print(f'Topological sort: {", ".join(str(i.node) for i in sorted_array)}')
    a, b, c, d = GraphNodeWeighted(2), GraphNodeWeighted(3), GraphNodeWeighted(5), GraphNodeWeighted(7)
    g = Graph([a, b, c, d])
    g.add_adjacent(a, c)
    g.add_adjacent(a, d)
    g.add_adjacent(c, b)
    #g.bfs(a)
    #g.dfs(a)
    print(f'printing weighted graph: {g.print()}')
    print("====Ended====")

>>>>>>> d1a5afd (feat - Add backtracking in python)
