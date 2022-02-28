class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return f'{self.cargo}'

