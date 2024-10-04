class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:
    def __init__(self, data):
        self.data = data
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = data

    def pop(self):
        if self.head is None:
            return None

        popped_node = self.head
        self.head = self.head.next
        return popped_node

    def peek(self):
        return self.head

    def is_empty(self):
        return bool(self.head)
