class Algorithm(object):
    HAS_CYCLE = False

    def calculate_shortest_path(self, vertex_list, edge_list, start_vertex):
        start_vertex.min_distance = 0

        for i in range(0, len(vertex_list) - 1):
            for edge in edge_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.predecessor = u

            for edge in edge_list:
                if self.has_cycle(edge):
                    print('Negative cycle detected')
                    Algorithm.HAS_CYCLE = True
                    return

    def has_cycle(self, edge) -> bool:
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            return True
        return False

    def get_shortest_path_to(self, target_vertex):
        if not Algorithm.HAS_CYCLE:
            print(f"Shortest path o target vertext: {target_vertex.min_distance}")
            node = target_vertex

            while node is not None:
                print(f'{node.name} ->')
                node = node.predecessor
