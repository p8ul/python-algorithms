from Vertex import Vertex
from Graph import Graph

g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs(a)
g.print_graph()