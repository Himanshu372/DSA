
class GraphNode:

    def __init__(self, val: int):
        self.node = val
        self.adjacent = []


class Graph:

    def __init__(self, nodes: list[GraphNode]):
        self.graph = nodes

    def add_adjacent(self, u: GraphNode, v: GraphNode):
        u.adjacent.append(v)
        v.adjacent.append(u)
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




if __name__ == "__main__":
    print("====Started====")
    a, b, c, d = GraphNode(2), GraphNode(3), GraphNode(5), GraphNode(7)
    g = Graph([a, b, c, d])
    g.add_adjacent(a, c)
    g.add_adjacent(a, d)
    g.add_adjacent(b, c)
    #g.bfs(a)
    g.dfs(a)
    print("====Ended====")

