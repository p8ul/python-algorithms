from Vertex import Vertex, BLACK, GREY, WHITE


class Graph(object):
    vertices = {}
    parents = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def print_graph(self):
        print('parents:', self.parents)
        for key in sorted(list(self.vertices.keys())):
            vertex = self.vertices[key]
            print(key + str(vertex.neighbors_names()) + " " + str(vertex.time), str(self.parents[key]))

    def add_parents(self, key, value):
        if key not in self.parents.keys():
            self.parents[key] = value

    def dfs(self, name):
        vertex = self.vertices[name]
        vertex.color = GREY
        if vertex.time[0] == -1:
            vertex.time[0] = self.time
            self.time += 1

        self.add_parents(name, None)

        for v in self.vertices[vertex.name].neighbors:
            if v.color == WHITE:
                self.add_parents(v.name, vertex.name)
                self.dfs(v.name)

        vertex.color = BLACK
        if vertex.time[1] == -1:
            vertex.time[1] = self.time
            self.time += 1
