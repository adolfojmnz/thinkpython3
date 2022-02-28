import re
from time import sleep
from Stack import Stack

def evaluate_postfix(expr):
    token_list = re.split('([^0-9])', expr)
    stack = Stack()

    for token in token_list:
        if token == ' ' or token == '':
            continue
        if token == '+':
            addition = stack.pop() + stack.pop()
            stack.push(addition)
        elif token == '-':
            sustraction = stack.pop() - stack.pop()
            stack.push(sustraction)
        elif token == '*':
            product = stack.pop() * stack.pop()
            stack.push(product)
        elif token == '/':
            divition = stack.pop() / stack.pop()
            stack.push(divition)
        else:
            stack.push(int(token))
    return stack.pop()


result = evaluate_postfix('3 2 * 1 + 2 *')
print(result)
