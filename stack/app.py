class Stack(object):
    def __init__(self):
        self._stack = []  # store internal list

    def is_empty(self):
        return len(self._stack) == 0

    def push(self, val):  # add to top of stack
        self._stack.insert(0, val)

    def top(self):  # peek current top value
        return self._stack[0]

    def pop(self):  # remove from the top of stack
        if len(self._stack) < 1:
            return None
        return self._stack.pop(0)

    def size(self):
        return len(self._stack)
