class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []


class Graph(object):
    def __init__(self, total_nodes):
        self.data = [[] for i in range(total_nodes)]

    def add_edge(self, fro_node, to_node):
        # minus one to make use of 0 index logic
        self.data[fro_node - 1].append(to_node - 1)
        self.data[to_node - 1].append(fro_node - 1)

    def adjacent_nodes(self, node) -> list:
        return self.data[node]


def bfs(n, edges, start):
    start = start - 1  # use 0 index

    visited = [False] * n
    distance = [-1] * n

    graph = Graph(n)
    for u, v in edges:
        graph.add_edge(u, v)

    visited[start] = True
    distance[start] = 0

    q = Queue()
    q.enqueue(start)

    while not q.is_empty():
        node = q.dequeue()
        visited[node] = True

        for adjacent_node in graph.adjacent_nodes(node):
            if visited[adjacent_node]:
                continue
            visited[adjacent_node] = True
            distance[adjacent_node] = 6 + distance[node]
            q.enqueue(adjacent_node)

    distance.remove(0)  # remove start distance
    return distance


total_nodes = 4
edges = [[1, 2], [1, 3]]
start = 1
t = bfs(total_nodes, edges, start)
print(t)
