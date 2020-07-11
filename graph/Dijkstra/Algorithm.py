import heapq


def calculate_shortest_path(start_vertex):
    queue = []
    start_vertex.min_distance = 0
    heapq.heappush(queue, start_vertex)

    while len(queue) > 0:
        actual_vertex = heapq.heappop(queue)

        for edge in actual_vertex.adjacent_list:
            u = edge.start_vertex
            v = edge.target_vertex

            new_distance = u.min_distance + edge.weight

            if new_distance < v.min_distance:
                v.predecessor = u
                v.min_distance = new_distance
                heapq.heappush(queue, v)


def get_shortest_path_to(target_vertex):
    print(f'Shortest path to target is: {target_vertex.min_distance}')

    node = target_vertex

    while node is not None:
        print(f'{node.name} ->')
        node = node.predecessor
