import operator


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, tag: dict):
        self.stack.append(tag)

    def last(self):
        print(f'stack: {self.stack}')

        if self.stack:
            print(f'last on stack: {self.stack[-1]}')
            return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)


class Storage:
    def __init__(self):
        self.storage = []

    def push(self, last_ul_ref):
        self.storage.append(last_ul_ref)
        print(f'storage: {self.storage}')

    def greatest_ul(self):
        all_uls = sorted(self.storage, key=operator.itemgetter('count'))
        return all_uls[-1]
