class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return bool(self.items)
