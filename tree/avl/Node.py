class Node(object):

    def __init__(self, data, parent_node):
        self.data = data
        self.parent_node = parent_node
        self.right_child = None
        self.left_child = None
        self.balance = 0

    def contains(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left_child is None:
                return False
            else:
                return self.left_child.contains(value)

        else:
            if self.right_child is None:
                return False
            else:
                return self.right_child.contains(value)

    def insert(self, data, parent_node):
        if data < self.data:
            if self.left_child is None:
                self.left_child = Node(data, parent_node)
            else:
                self.left_child.insert(data, parent_node)

        else:
            if self.right_child is None:
                self.right_child = Node(data, parent_node)

            else:
                self.right_child.insert(data, parent_node)
        return parent_node

    def traverse_in_order(self):
        if self.left_child:
            self.left_child.traverse_in_order()
        print(self.data)

        if self.right_child:
            self.right_child.traverse_in_order()

    def get_max(self):
        if not self.right_child:
            return self.data
        else:
            return self.right_child.get_max()

    def get_min(self):
        if not self.left_child:
            return self.data
        else:
            return self.left_child.get_min()

    def has_left_child(self, node):
        return True if node.left_child else False

    def has_right_child(self, node):
        return True if node.right_child else False

    def has_children(self, node):
        return self.has_right_child(node) and self.has_left_child(node)

    def has_left_or_right_child(self, node):
        return self.has_right_child(node) or self.has_left_child(node)

    def print_left_child(self, node):
        print('[Left]:', node.left_child.data)

    def print_right_child(self, node):
        print('[Right]:', node.right_child.data)

    def print_nodes(self, node):
        if self.has_left_or_right_child(node):
            print(f'\n[Parent]: {node.data}')
        if self.has_left_child(node):
            self.print_left_child(node)
        if self.has_right_child(node):
            self.print_right_child(node)
        if self.has_left_child(node):
            node.left_child.print_nodes(node.left_child)
        if self.has_right_child(node):
            node.right_child.print_nodes(node.right_child)
