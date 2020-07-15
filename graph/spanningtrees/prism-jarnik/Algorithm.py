import heapq

from Vertex import Vertex


class Algorithm(object):
    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.spanning_tree = []
        self.edge_heap = []
        self.full_cost: int = 0

    def construct_spanning_tree(self, vertex: Vertex):
        self.unvisited_list.remove(vertex)

        while self.unvisited_list:
            for edge in vertex.adjacent_list:
                if edge.target_vertex in self.unvisited_list:
                    heapq.heappush(self.edge_heap, edge)

            min_edge = heapq.heappop(self.edge_heap)

            self.spanning_tree.append(min_edge)
            print(f'Edge added to spanning tree: {min_edge.start_vertex.name} - {min_edge.target_vertex.name}')
            self.full_cost += min_edge.weight

            vertex = min_edge.target_vertex
            self.unvisited_list.remove(vertex)

    def get_spanning_tree(self):
        return self.spanning_tree
