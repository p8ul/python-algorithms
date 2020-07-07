class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, data):
        if data < self.data:
            if self.left_child is None:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if self.right_child is None:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)

    def remove(self, data, parent_node):
        if data < self.data:
            if self.left_child is not None:
                self.left_child.remove(data, self)
        elif data > self.data:
            if self.right_child is not None:
                self.right_child.remove(data, parent_node)
        else:
            if self.left_child is not None and self.right_child is not None:
                self.data = self.right_child.get_min()
                self.right_child.remove(self.data, self)

            elif parent_node.left_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node.left_child = temp_node

            elif parent_node.right_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child

                parent_node.right_child = temp_node

    def get_min(self):
        if self.left_child is None:
            return self.data
        else:
            self.left_child.getMin()

    def get_max(self):
        if self.right_child is None:
            return self.data
        else:
            return self.right_child.get_max()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()

        print(self.data)
        if self.right_child is not None:
            self.right_child.traverse_in_order()
