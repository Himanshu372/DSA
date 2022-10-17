class SetNode(object):
    """
    Wrapper class for implementing Disjoint set nodes
    """
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


class DisjointSets(object):
    """
    Class implementing basic functionality of Disjoint sets. Implements the main method for Disjoint sets,
    which is find() and union(). Union operation is implemented using rank heuristic. Disjoint sets main application
    is in Kruskal's algo and finding cycle in given graph.
    """
    def __init__(self):
        self.members = {}

    def __repr__(self):
        l = {}
        for each in self.members.values():
            if each.parent.value == each.value:
                l[each] = []
                l[each].append(each.value)
        for each in self.members.values():
            if each.parent.value != each.value:
                l[each.parent].append(each.value)
        return ' '.join(str(value) for value in l.values())

    def make_set(self, val):
        if val not in self.members:
            self.members[val] = SetNode(val)
            return True
        return False

    def find(self, value):
        if value in self.members:
            return self.members[value].parent
        return False

    def union(self, v1, v2):
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)

        if root_v1 == root_v2:
            return
        if root_v1.rank > root_v2.rank:
            root_v2.parent = root_v1
        elif root_v1.rank < root_v2.rank:
            root_v1.parent = root_v2
        else:
            root_v2.parent = root_v1
            root_v1.rank += 1


if __name__=='__main__':
    st = DisjointSets()
    for i in range(4):
        st.make_set(i)
    print(st)
    st.union(1, 3)
    st.union(3, 2)
    st.union(0, 3)
    print(st)