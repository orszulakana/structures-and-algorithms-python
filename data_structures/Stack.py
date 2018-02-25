class Stack:

    # constructor
    def __init__(self):
        self.stack = []

    # add element
    def push(self, element):
        self.stack.append(element)

    # remove element
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.stack.pop(len(self.stack) - 1)

    # get last element
    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
