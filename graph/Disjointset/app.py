from collections import defaultdict


class Graph:
    """
    # Python Program for union-find algorithm to detect cycle in a undirected graph
    # we have one edge for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both
    # https://www.geeksforgeeks.org/union-find/
    # https://www.youtube.com/watch?v=wU6udHRIkcc&ab_channel=AbdulBari
    """

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)

    # add edge to Graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    # The main function to check whether a given graph
    # contains cycle of not
    def isCyclic(self):
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sum
        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in Graph
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
