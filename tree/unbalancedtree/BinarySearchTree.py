from Node import Node


class BST(object):
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, data_to_remove):
        if self.rootNode:
            if self.rootNode.data == data_to_remove:
                temp_node = Node(None)
                temp_node.left_child = self.rootNode
                self.rootNode.remove(data_to_remove, temp_node)
            else:
                self.rootNode.remove(data_to_remove, None)

    def get_max(self):
        if self.rootNode:
            return self.rootNode.get_max()

    def get_min(self):
        if self.rootNode:
            return self.rootNode.get_min()

    def traverse_in_order(self):
        if self.rootNode:
            return self.rootNode.traverse_in_order()
