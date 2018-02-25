class Queue:
    def __init__(self):
        self.queue = [];

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0
