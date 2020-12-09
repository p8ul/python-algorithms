# colors
WHITE = 'WHITE'
BLACK = 'BLACK'
GREY = 'GREY'


class Vertex:
    def __init__(self, name, color):
        self.name = name
        self.neighbors = []
        self.parent = None
        self.distance = 0
        self.color = WHITE
        self.node_color = color
        self.time = [-1, -1]

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors = sorted(self.neighbors, key=lambda i: i.name)
            self.add_parent(vertex)

    def add_parent(self, vertex):
        vertex.parent = self.name

    def neighbors_names(self):
        x = []
        [x.append(v.name) for v in self.neighbors]
        return x

    def parent_name(self):
        print(self.name, self.parent)
        if self.parent:
            return self.parent
        return self.parent


class Graph(object):
    vertices = {}
    parents = {}
    time = 0

    def __init__(self, node_color):
        self.node_color = node_color

    def add_vertex(self, vertex):
        self.vertices[vertex.name] = vertex

    def dfs(self, name):
        vertex = self.vertices[name]
        print(vertex.name, vertex.neighbors_names())
        vertex.color = GREY

        if vertex.time[0] == -1:
            vertex.time[0] = self.time
            self.time += 1

        for v in self.vertices[vertex.name].neighbors:
            if v.node_color == self.node_color:
                print('found color in node ', v.name)
                # break
            if v.color == WHITE:
                self.dfs(v.name)

        vertex.color = BLACK
        if vertex.time[1] == -1:
            vertex.time[1] = self.time
            self.time += 1

    def print_graph(self):
        print('parents:', self.parents)
        for key in sorted(list(self.vertices.keys())):
            vertex = self.vertices[key]
            print(self.parents)
            print(str(key) + str(vertex.neighbors_names()) + " " + str(vertex.time), str(self.parents[key]))


vertex1 = Vertex(1, 1)

vertex2 = Vertex(2, 2)

vertex3 = Vertex(3, 1)
vertex4 = Vertex(4, 1)
vertex1.add_neighbor(vertex2)
vertex1.add_neighbor(vertex3)
vertex2.add_neighbor(vertex4)

all_v = [vertex1, vertex2, vertex3, vertex4]
graph = Graph(1)
for i in all_v:
    graph.add_vertex(i)

# graph.print_graph()
graph.dfs(1)
print(graph.time, 'is the time taken')
for v in graph.vertices:
    print(graph.vertices[v].name, graph.vertices[v].neighbors_names(), graph.vertices[v].color)

distance = 0
g_from = 1
