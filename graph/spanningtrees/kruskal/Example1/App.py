from Algorithm import Algorithm
from Vertex import Vertex
from Edge import Edge

vertexA = Vertex("a")
vertexB = Vertex("b")
vertexC = Vertex("c")
vertexD = Vertex("d")
vertexE = Vertex("e")
vertexF = Vertex("f")

edge1 = Edge(2, vertexA, vertexB)
edge2 = Edge(4, vertexA, vertexD)
edge3 = Edge(4, vertexB, vertexC)
edge4 = Edge(4, vertexB, vertexD)
edge5 = Edge(3, vertexB, vertexE)
edge6 = Edge(1, vertexB, vertexF)
edge7 = Edge(5, vertexC, vertexF)
edge8 = Edge(2, vertexD, vertexE)
edge9 = Edge(5, vertexE, vertexF)

vertex_list: [Vertex] = list()

vertex_list.append(vertexA)
vertex_list.append(vertexB)
vertex_list.append(vertexC)
vertex_list.append(vertexD)
vertex_list.append(vertexE)
vertex_list.append(vertexF)

edge_list: [Edge] = list()

edge_list.append(edge1)
edge_list.append(edge2)
edge_list.append(edge3)
edge_list.append(edge4)
edge_list.append(edge5)
edge_list.append(edge6)
edge_list.append(edge7)
edge_list.append(edge8)
edge_list.append(edge9)

algorithm = Algorithm()

algorithm.construct_spanning_tree(vertex_list, edge_list)
