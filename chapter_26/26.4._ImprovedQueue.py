class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return f'{self.cargo}'


class ImprovedQueue:

    def __init__(self):
        self.head = None
        self.last = None
        self.lenght = 0

    def print_queue(self):
        head = self.head
        print(f'Queue:\n{head}')

        if self.lenght > 0:
            while head.next:
                head = head.next
                print(head)
        return

    def is_empty(self):
        return self.lenght == 0

    def insert(self, cargo):
        node = Node(cargo)

        if self.head is None:
            self.head = self.last = node
        else:
            self.last.next = self.last = node

        self.lenght += 1

    def remove(self):
        head = self.head

        if self.lenght == 0:
            self.head = self.last = None
        else:
            self.head = self.head.next
            self.lenght -= 1

        return f'{head}'


if __name__ == '__main__':

    queue = ImprovedQueue()
    queue.insert(8)
    queue.insert(5)
    queue.insert(3)
    queue.insert(2)

    (queue.remove())
    queue.print_queue()

    (queue.remove())
    queue.print_queue()


