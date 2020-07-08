from Vertex import Vertex
from Graph import Graph


adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}

g = Graph()
vertex = Vertex('A')
for key, values in adj_list.items():
    vertex = Vertex(key)

    [vertex.add_neighbor(Vertex(i)) for i in values]
    g.add_vertex(vertex)

g.dfs('A')
g.print_graph()

