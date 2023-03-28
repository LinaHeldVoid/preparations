
class Stack:

    def __init__(self, data):
        self.stack = data

    def is_empty(self):
        if self.stack is None:
            result = True
        else:
            result = False
        return result

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        self.stack.pop(-1)
        last_element = self.stack[-1]
        return last_element

    def peek(self):
        last_element = self.stack[-1]
        return last_element

    def size(self):
        size = len(self.stack)
        return size
