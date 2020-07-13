from DisjointSet import DisjointSet


class Algorithm(object):

    def construct_spanning_tree(self, vertext_list, edge_list):
        disjointset = DisjointSet(vertext_list)
        spanning_tree = []

        edge_list.sort()

        for edge in edge_list:
            u = edge.start_vertex
            v = edge.target_vertex

            if disjointset.find(u.parent_node) is not disjointset.find(v.parent_node):
                spanning_tree.append(edge)
                disjointset.union(u.parent_node, v.parent_node)

        for edge in spanning_tree:
            print(edge.start_vertex.name, '-', edge.target_vertex.name)
