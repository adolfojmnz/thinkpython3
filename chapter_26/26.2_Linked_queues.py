class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return f'{self.cargo}'


class Queue:
    """ Create a queue with the FIFO policy. """

    def __init__(self):
        self.head = None
        self.lenght = 0

    def __str__(self):
        return f'{self.head}'

    def is_empty(self):
        return self.lenght == 0

    def insert(self, cargo):
        node = Node(cargo)

        if self.head is None:
            # first element on the queue.
            self.head = node
        else:
            last = self.head
            while last.next:
                # loops until last.next is None
                last = last.next
            # append the node at the end of the queue.
            last.next = node
        self.lenght += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.lenght -= 1
        return cargo


queue = Queue()
queue.insert([3, 5])
print(queue.remove())

n1 = Node(0)
n2 = Node(0)
print(n1 == n2)
