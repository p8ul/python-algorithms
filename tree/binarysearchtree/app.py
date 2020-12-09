from random import shuffle


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


tree = BinarySearchTree()

arr = [i for i in range(1, 8)]
shuffle(arr)
print(arr)

for i in range(len(arr)):
    tree.create(arr[i])

print(height(tree.root), ': max height')
