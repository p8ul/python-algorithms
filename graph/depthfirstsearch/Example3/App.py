#!/usr/bin/env python3

from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from Node import Node
from DFS import dfs

node1: Node = Node('A')
node2: Node = Node('B')
node3: Node = Node('C')
node4: Node = Node('D')
node5: Node = Node('E')

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node2.adjacent_list.append(node4)
node4.adjacent_list.append(node5)

dfs(node1)
