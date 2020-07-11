import sys


class Node(object):
    def __init__(self, name: str):
        self.name: str = name
        self.visited: bool = False
        self.adjacent_list: [Node] = []
        self.predecessor = None
        self.min_distance = sys.maxsize
