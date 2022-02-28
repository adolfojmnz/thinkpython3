class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        return f'{self.items}'

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


stack = Stack()

stack.push(')')
stack.push(44)
stack.push('+')
stack.push(4.4)
stack.push('(')
stack.push('=')
stack.push(48.4)

while not stack.is_empty():
    print(stack.pop(), end=' ')
