class MaxHeap:
    """
     Max Heap: Each Node at index (i) has:
     it's children at indices (2i + 1) and (2i + 2)
     and parent at index floor((i - 1) / 2)
    """

    def __init__(self):
        self.heap = []

    def get_parent(self, i):
        return int((i - 1) / 2)

    def get_left_child(self, i):
        return 2 * i + 1

    def get_right_child(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent(i) >= 0

    def has_children(self, i):
        return self.has_right_child(i) and self.has_left_child(i)

    def has_left_child(self, i):
        return self.get_left_child(i) < len(self.heap)

    def has_right_child(self, i):
        return self.get_right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert_key(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def delete_root(self):
        """ swap last item with first item then heapify down """
        if len(self.heap) == 0:
            return -1

        last_index = len(self.heap) - 1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        while self.has_left_child(i):
            max_child_index = self.get_max_child_index(i)
            if max_child_index == -1:
                break
            if self.heap[i] < self.heap[max_child_index]:
                self.swap(i, max_child_index)
                i = max_child_index
            else:
                break

    def get_max_child_index(self, i):
        if self.has_left_child(i):
            left_child = self.get_left_child(i)
            if self.has_right_child(i):
                right_child = self.get_right_child(i)
                if self.heap[left_child] > self.heap[right_child]:
                    return left_child
                else:
                    return right_child
        else:
            return -1

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]:
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)

    def print_heap(self):
        print(self.heap)
        for i in range(0, len(self.heap)):
            if self.has_children(i):
                print('[P]: ', self.heap[i])
                self.print_children(i)
            elif self.has_right_child(i):
                print('         [R]:', self.heap[self.get_right_child(i)])
            elif self.has_left_child(i):
                print('[L]:', self.heap[self.get_left_child(i)])

    def print_children(self, i):
        print('[L]:', self.heap[self.get_left_child(i)], '     [R]:', self.heap[self.get_right_child(i)])


heap = MaxHeap()
heap.insert_key(99)
heap.insert_key(50)
heap.insert_key(63)
heap.insert_key(35)
heap.insert_key(45)
heap.insert_key(57)
heap.insert_key(42)
heap.insert_key(27)
heap.insert_key(12)
heap.insert_key(24)
heap.insert_key(29)
heap.delete_root()
heap.print_heap()
