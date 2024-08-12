import operator


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, tag: dict):
        self.stack.append(tag)

    def last(self):
        if self.stack:
            return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True
