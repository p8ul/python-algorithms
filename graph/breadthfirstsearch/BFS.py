from queue import Queue

adj_list = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"],
}

visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s] = 0

queue.put(s)

while not queue.empty():
    u = queue.get()

    bfs_traversal_output.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print('traversal', bfs_traversal_output)


# shortest distance of all nodes from source node
print(f'All node distance : {level}')
print(f'Path to G is {level["G"]}')  # 3
print(f'All parents :{parent}')
# shortest path of node from source node
v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent[v]

path.reverse()
print(f'shortest path of {v}  is {path}')

