from Vertex import Vertex
from Edge import Edge
from Algorithm import Algorithm

vertex1 = Vertex('1')
vertex2 = Vertex('2')
vertex3 = Vertex('3')
vertex4 = Vertex('4')

edge1 = Edge(1, vertex1, vertex2)
edge2 = Edge(1, vertex1, vertex3)
edge3 = Edge(0.01, vertex1, vertex4)
edge4 = Edge(1, vertex3, vertex4)

vertex1.adjacent_list.append(edge1)
vertex1.adjacent_list.append(edge2)
vertex1.adjacent_list.append(edge3)
vertex3.adjacent_list.append(edge4)

unvisited_list = list()

unvisited_list.append(vertex1)
unvisited_list.append(vertex2)
unvisited_list.append(vertex3)
unvisited_list.append(vertex4)

algorithm = Algorithm(unvisited_list)
algorithm.construct_spanning_tree(vertex1)
print(algorithm.get_spanning_tree())
