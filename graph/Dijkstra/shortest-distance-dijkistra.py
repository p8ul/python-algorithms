import sys
import heapq


def dijkstra(total_nodes, graph, start):
    visited = set()
    # initialize the initial distance of the edges to infinity (max syssize for this case)
    distance = {i: sys.maxsize for i in range(1, total_nodes + 1)}

    queue = [(distance[i], i) for i in range(1, total_nodes + 1)]
    distance[start] = 0  # distance of starting node should be zero

    heapq.heappush(queue, (0, start))  # give the start node the smallest distance 0
    while queue:
        current_node_weight, node = heapq.heappop(queue)

        if node in visited:
            continue
        # calculate distance of adjacent nodes
        for adj_node, weight in graph[node]:
            if distance[adj_node] > current_node_weight + weight:
                distance[adj_node] = current_node_weight + weight
                heapq.heappush(queue, (distance[adj_node], adj_node))  # add adj node to the queue
        visited.add(node)
    return distance


# Complete the shortestReach function below.
def shortestReach(total_nodes, total_edges, edges, start_node):
    # represent your graph as a dictionary where key denotes the node
    # e.g {1: [], 2: []}
    graph = {i: [] for i in range(1, total_nodes + 1)}

    # add nodes with their adjacent nodes & weight in your graph
    # eg. {1: [(2, 24), (4, 20), (3, 3)], 2: [(1, 24)], 3: [(1, 3), (4, 12)], 4: [(1, 20), (3, 12)]}
    for i in range(0, total_edges):
        node1, node2, weight = edges[i]
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))

    distance = dijkstra(total_nodes, graph, start_node)

    # traverse the shortest distance
    res = []
    for i, value in distance.items():
        if value != 0 and value != sys.maxsize:
            print(value, end=" ")
            res.append(value)
        elif value == sys.maxsize:
            print('-1', end=" ")
            res.append(-1)
    return res


if __name__ == "__main__":
    total_nodes = 4
    total_edges = 4
    edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
    start_node = 1
    shortestReach(total_nodes, total_edges, edges, start_node)
