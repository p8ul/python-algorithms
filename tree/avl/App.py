from BalancedTree import BalancedTree

tree = BalancedTree()

tree.insert(4)
tree.insert(6)
tree.insert(5)
tree.insert(7)
# tree.insert(8)

print('sum of deepest leaves: ', tree.sum_of_deepest_leaves())
print('parent node: ', tree.root_node.data)
tree.print_nodes()
