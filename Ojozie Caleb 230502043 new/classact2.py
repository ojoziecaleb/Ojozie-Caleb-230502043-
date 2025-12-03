class ArrayStack:
    def _init_(self):
        self.data = []

    def push(self, x):
        self.data.append(x)   # amortized O(1)

    def pop(self):
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        return None if not self.data else self.data[-1]

    def is_empty(self):
        return len(self.data) == 0
class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def _init_(self):
        self.top = None

    def push(self, x):
        node = Node(x)
        node.next = self.top
        self.top = node      # O(1)

    def pop(self):
        if not self.top:
            raise IndexError("pop from empty stack")
        val = self.top.value
        self.top = self.top.next
        return val

    def peek(self):
        return None if not self.top else self.top.value