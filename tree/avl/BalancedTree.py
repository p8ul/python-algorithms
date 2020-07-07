from Node import Node


class BalancedTree(object):

    def __init__(self):
        self.root_node = None

    def contains(self, data):
        return self.root_node.contains(data)

    def print_nodes(self):
       self.root_node.print_nodes(self.root_node)

    def insert(self, data):

        if self.root_node is None:
            parent_node = Node(data, None)
            self.root_node = parent_node
        else:
            parent_node = self.root_node.insert(data, self.root_node)

        self.re_balance_tree(parent_node)

    def re_balance_tree(self, parent_node):
        self.set_balance(parent_node)

        if parent_node.balance < -1:
            if self.height(parent_node.left_child.left_child) >= self.height(parent_node.left_child.right_child):
                parent_node = self.rotate_right(parent_node)
            else:
                parent_node = self.rotate_left_right(parent_node)
        elif parent_node.balance > 1:
            if self.height(parent_node.right_child.right_child) >= self.height(parent_node.right_child.left_child):
                parent_node = self.rotate_left(parent_node)
            else:
                parent_node = self.rotate_right_left(parent_node)

        if parent_node.parent_node is not None:
            self.re_balance_tree(parent_node.parent_node)
        else:
            self.root_node = parent_node

    def rotate_left_right(self, node):
        print("Rotation left right...")
        node.left_child = self.rotate_left(node.left_child)
        return self.rotate_right(node)

    def rotate_right_left(self, node):
        print("Rotation right left...")
        node.right_child = self.rotate_right(node.right_child)
        return self.rotate_left(node)

    def rotate_left(self, node):
        print('Rotate left')
        b = node.right_child
        b.parent_node = node.parent_node

        node.right_child = b.left_child
        if node.right_child is not None:
            node.right_child.parent_node = node

        b.left_child = node
        node.parent_node = b
        if b.parent_node is not None:
            if b.parent_node.right_child == node:
                b.parent_node.right_child = b
            else:
                b.parent_node.left_child = b
        self.set_balance(node)
        self.set_balance(b)

        return b

    def rotate_right(self, node):
        print('Rotate right....')
        b = node.left_child
        b.parent_node = node.parent_node

        node.left_child = b.right_child

        if node.left_child is not None:
            node.left_child.parent_node = node

        b.right_child = node
        node.parent_node = b

        if b.parent_node is not None:
            if b.parent_node.right_child == node:
                b.parent_node.right_child = b
            else:
                b.parent_node.left_child = b

        self.set_balance(node)
        self.set_balance(b)

        return b

    def set_balance(self, node):
        node.balance = (self.height(node.right_child) - self.height(node.left_child))

    def height(self, node):
        if node is None:
            return -1
        else:
            return 1 + max(self.height(node.left_child), self.height(node.right_child))

    def sum_of_deepest_leaves(self) -> int:
        q, last_level = [self.root_node], []
        count = 0
        while q:
            next_level = []
            n = len(q)
            for _ in range(n):
                node = q.pop()
                for child in node.left_child, node.right_child:
                    if child:
                        next_level.append(child)

                q = next_level
                if next_level:
                    last_level = next_level[:]
            count += 1
            return sum(node.data for node in last_level)
