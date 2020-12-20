class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.enqueue(4)
q.enqueue('world')
q.dequeue()
q.dequeue()
print(q.items)
