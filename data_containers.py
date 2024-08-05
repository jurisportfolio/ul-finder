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


class Storage:
    def __init__(self):
        self.storage = []

    def push(self, last_ul):
        self.storage.append(last_ul)

    def greatest_ul(self):
        all_uls = sorted(self.storage, key=operator.itemgetter('count'))
        return all_uls[-1]
