class Vertex(object):
    def __init__(self, name: str):
        self.name: str = name
        self.visited: bool = False
        self.predecessor = None
        self.adjacent_list: [Vertex] = []
