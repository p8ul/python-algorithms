class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

        self.distance = 9999
        self.color = 'black'

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()

