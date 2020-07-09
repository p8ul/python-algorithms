#!/usr/bin/env python3
from Node import Node


def dfs(node: Node):
    node.visited = True
    print(f'{node.name} ->')

    for n in node.adjacent_list:
        if not n.visited:
            dfs(n)
