"""
  1)   Write an implementation of the Queue ADT using a Python list.
     Compare the performance of this implementation to the ImprovedQueue
     for a range of queue lengths.
"""


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

    def is_empty(self):
        return self.lenght == 0

    def insert(self, _list):
        _list.sort()
        for item in _list:
            node = Node(item)

            if self.head is None:
                self.head = node
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = node
            self.lenght += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.lenght -= 1
        return cargo


queue = Queue()
queue.insert([3, 5])

while not queue.is_empty():
    print(queue.remove())
