"""
  2)   Write an implementation of the Priority Queue ADT using a linked
     list. You should keep the list sorted so that removal is a constant
     time operation. Compare the performance of this implementation with
     the Python list implementation.
"""


from Node import Node

def linkedList(_list):
    _list.sort()
    output = []

    for i,v in enumerate(_list):
        node = Node(v)
        output.append(node)

        if len(output) > 1:
            output[i-1].next = output[i].cargo
    return output


class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, _list):
        self.items = _list

    def remove(self):
        if not self.is_empty():
            return self.items.pop(0)

if __name__ == '__main__':

    from time import time

    t0 = time()

    some_list = linkedList([2, 5, 8, 3, 7])
    queue = PriorityQueue()
    queue.insert(some_list)

    t1 = time()
    print(f'time: {(t1-t0)*1000:.3f}e-3 secs.')

