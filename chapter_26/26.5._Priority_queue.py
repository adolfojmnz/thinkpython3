class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        greater = 0

        for index in range(1, len(self.items)):
            if self.items[index] > self.items[greater]:
                greater = index

        item = self.items[greater]
        del self.items[greater]
        return item


queue = PriorityQueue()

for item in [14, 77, 53, 28]:
    queue.insert(item)

while not queue.is_empty():
    print(queue.remove())
