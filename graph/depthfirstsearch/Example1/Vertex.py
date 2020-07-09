import collections

# colors
WHITE = 'WHITE'
BLACK = 'BLACK'
GREY = 'GREY'


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.distance = 0
        self.color = WHITE
        self.time = [-1, -1]

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors = sorted(self.neighbors, key=lambda i: i.name)

    def neighbors_names(self):
        x = []
        [x.append(v.name) for v in self.neighbors]
        return x

    def parent_name(self):
        print(self.name, self.parent)
        if self.parent:
            return self.parent
        return self.parent
