class Queue():

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items = [item] + self.items

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]
