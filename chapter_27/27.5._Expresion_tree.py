import re
from Tree import Tree


def print_tree_inorderer(tree):
    if tree is None: return
    print_tree_inorderer(tree.left)
    print(tree.cargo, end=' ')
    print_tree_inorderer(tree.right)


def tokenize_list(string):
    ss = re.split('', string)

    for (i,v) in enumerate(ss):
        if v in ['(', ')']:
            del ss[i]
    ss = re.split(' ', ''.join(ss))

    for (i,v) in enumerate(ss):
        if v not in '+-*/':
            ss[i] = int(v)
    ss.append('end')
    return ss


def get_token(token_list):
    operators = list('+-*/')
    if token_list[0] in operators:
        return True
    return False

def get_operator(token_list):
    operator = token_list[0]
    del token_list[0]
    return operator


def get_number(token_list):
    n = token_list[0]
    if type(n) != type(0):
        return None
    del token_list[0]
    return Tree(n, None, None)


def get_operation(token_list):
    n = get_number(token_list)
    if get_token(token_list):
        operator = get_operator(token_list)
        m = get_operation(token_list)
        return Tree(operator, n, m)
    return n


token_list = tokenize_list('(9 * 11) + (5 * 7) - (1 / 3)')

tree = get_operation(token_list)
print_tree_inorderer(tree)

