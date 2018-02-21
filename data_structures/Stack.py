class Stack:

    # constructor
    def __init__(self):
        self.Stack = []

    # add element
    def Push(self, element):
        self.Stack.append(element)

    # remove element
    def Pop(self):
        self.Stack.pop(len(self.Stack) - 1)

    # stack size
    def Size(self):
        return len(self.Stack)

    # get last element
    def Top(self):
        return self.Stack[len(self.Stack) - 1]

    def Empty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False