# 24.2 The Node class
class Node:

    def __init__(self, cargo=None, _next=None):
        self.cargo = cargo
        self.next = _next

    def __str__(self):
        return f'{self.cargo}'

# 24.3 Lists as collections
def print_list(node):
    print('[', end=' ')
    while node is not None:
        if node.next is not None:
            s = ', '
        else:
            s = ' '
        print(node, end=s)
        node = node.next
    print(']')

# 24.4 Lists and recursion
def print_backwards(_list):
    if _list is not None:
        head = _list
        tail = _list.next
        print_backwards(tail)
        print(head, end=' ')
    return

# 24.7 Modififying lists
def remove_second(_list):
    if _list is not None:
        first = _list
        second = _list.next
        # Make the first node refer to the third
        first.next = second.next
        # Separate the second from the rest of the list
        second.next = None
        return second
    return

def print_backwards_nicely(_list):
    print('[', end=' ')
    print_backwards(_list)
    print(']')

if __name__ == '__main__':
    (node1, node2, node3) = (Node(1), Node(2), Node(3),)
    (node1.next, node2.next) = (node2, node3)

    print_list(node1)

