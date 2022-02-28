class LinkedList:

    def __init__(self):
        self.lenght = 0
        self.head = None

    def __str__(self):
        head = self.head
        _next = self.head.next
        tail = _next.next

        return f'[{head}]'

    def print_backwards(self):
        print('[', end=' ')
        if self.head is not None:
            self.head.print_backwards()
        print(']')

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.lenght += 1


class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return f'{self.cargo}'

    def print_backwards(self):
        if self.next is not None:
            tail = self.next
            tail.print_backwards()

        try:
            if self.next.next is not None:
                s = ' '
            else:
                raise
        except:
            s = ', '
        print(self.cargo, end=s)


if __name__ == '__main__':
    from time import time

    t0 = time()

    linked1 = LinkedList()
    linked1.add_first(2)
    linked1.add_first(3)
    linked1.add_first(5)
    linked1.add_first(7)
    linked1.add_first(8)

    t1 = time()

    print(f'time: {(t1-t0)*1000:.3f}e-3 secs.')
