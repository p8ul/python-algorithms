adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# visited vertices
# W - not visited
# G - first visited
# B - fully explored
color = {}  # W, G, B

# parent of the vertex
parent = {}

# when a node is first visited and when it's fully visited
traverse_time = {}  # [start, end]

dfs_traversal_output = []

# initialiaze variables
for node in adj_list.keys():
    color[node] = 'W'
    parent[node] = None
    traverse_time[node] = [-1, -1]

time = 0


def dfs_util(u):
    global time
    color[u] = "G"
    traverse_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1
    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs_util(v)
    color[u] = "B"
    traverse_time[u][1] = time
    time += 1


dfs_util('A')

for u in adj_list.keys():
    if color[u] == 'W':
        dfs_util(u)

for node in adj_list.keys():
    print(node, ' -> ', traverse_time[node])

print(color)
print(parent)
print(dfs_traversal_output)
