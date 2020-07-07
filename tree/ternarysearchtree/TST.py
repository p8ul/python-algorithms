from Node import Node


class TST(object):
    def __init__(self):
        self.root_node = None

    def put(self, key, value):
        self.root_node = self.put_item(self.root_node, key, value, 0)

    def put_item(self, node, key, value, index):
        c = key[index]
        if node is None:
            node = Node(c)
        if c < node.character:
            node.left_node = self.put_item(node.left_node, key, value, index)
        elif c > node.character:
            node.right_node = self.put_item(node.right_node, key, value, index)

        elif index < len(key) - 1:
            node.middle_node = self.put_item(node.middle_node, key, value, index + 1)
        else:
            node.value = value

        print(node.__dict__)
        return node

    def get(self, key):
        node = self.get_item(self.root_node, key, 0)
        if node is None:
            return None
        else:
            return node.value

    def get_item(self, node, key, index):
        if node is None:
            return None

        c = key[index]
        if c < node.character:
            return self.getItem(node.left_node, key, index)
        elif c > node.character:
            return self.get_item(node.right_node, key, index)
        elif index < len(key) - 1:
            return self.get_item(node.middle_node, key, index + 1)
        return node
