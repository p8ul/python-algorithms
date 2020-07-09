from typing import List


class Node(object):

    def __init__(self, name):
        self.name: str = name
        self.adjacent_list: List[Node] = []
        self.visited: bool = False
