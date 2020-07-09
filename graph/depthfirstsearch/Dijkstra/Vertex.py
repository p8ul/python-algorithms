from typing import List
import sys


class Vertex(object):
    def __init__(self, name: str):
        self.name: str = name
        self.visited: bool = False
        self.predecessor = None
        self.adjacent_list: List[Vertex] = []
        self.min_distance = sys.maxsize

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority
