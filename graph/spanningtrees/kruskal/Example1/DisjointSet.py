from Node import Node
from Vertex import Vertex


class DisjointSet(object):

    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = []
        self.node_count = 0
        self.set_count = 0
        self.make_sets(vertex_list)

    def find(self, node):
        current_node = node

        while hasattr(current_node, 'parentNode') and current_node.parent_node is not None:
            current_node = current_node.parent_node

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent_node
            current_node.parent_node = root
            current_node = temp

        return root.node_id

    def union(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.height < root2.height:
            root1.parent_node = root2
        elif root1.height > root2.height:
            root2.parent_node = root1
        else:
            root2.parent_node = root1
            root1.height += 1

        self.set_count -= 1

    def make_sets(self, vertex_list):
        for v in vertex_list:
            self.make_set(v)

    def make_set(self, vertex: Vertex):
        node = Node(0, len(self.root_nodes), Node)
        vertex.parent_node = node
        self.root_nodes.append(node)
        self.set_count += 1
        self.node_count += 1
