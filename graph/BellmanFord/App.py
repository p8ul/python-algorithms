from Algorithm import Algorithm
from Node import Node
from Edge import Edge

node1: Node = Node("A")
node2: Node = Node("B")
node3: Node = Node("C")
node4: Node = Node("D")

edge1: Edge = Edge(1, node1, node2)
edge2: Edge = Edge(1, node2, node3)
edge3: Edge = Edge(1, node3, node4)
edge4: Edge = Edge(-4, node3, node2)
edge5: Edge = Edge(0.01, node1, node4)

node1.adjacent_list.append(edge1)
node1.adjacent_list.append(edge2)
node2.adjacent_list.append(edge3)
node3.adjacent_list.append(edge4)
node3.adjacent_list.append(edge2)

vertex_list = [node1, node2, node3, node4, ]
edge_list = [edge1, edge2, edge3, edge4, edge5]

algorithm = Algorithm()
algorithm.calculate_shortest_path(vertex_list, edge_list, node1)
algorithm.get_shortest_path_to(node4)
