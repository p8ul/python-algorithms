from Algorithm import calculate_shortest_path, get_shortest_path_to
from Vertex import Vertex
from Edge import Edge

vertex1: Vertex = Vertex('A')
vertex2: Vertex = Vertex('B')
vertex3: Vertex = Vertex('C')

edge1 = Edge(1, vertex1, vertex2)
edge2 = Edge(1, vertex2, vertex3)
edge3 = Edge(11, vertex1, vertex3)

vertex1.adjacent_list.append(edge1)
vertex1.adjacent_list.append(edge2)
vertex2.adjacent_list.append(edge3)

vertex_list = {vertex1, vertex2, vertex3}

calculate_shortest_path(vertex1)

get_shortest_path_to(vertex3)
