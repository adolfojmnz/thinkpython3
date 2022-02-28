import re
from Tree import Tree


def print_tree_postorder(tree):
    if tree is None:
        return
    print_tree_postorder(tree.left)
    print(tree.cargo, end=' ')
    print_tree_postorder(tree.right)


def tokenize_list(string):
    ss = re.split('', string)
    for (i,v) in enumerate(ss):
        if v in ['(', ')']:
            del ss[i]
    ss = re.split(' ', ''.join(ss))
    for (i,v) in enumerate(ss):
        try:
            if type(int(v)) == type(0):
                ss[i] = int(v)
        except: continue
    return ss


def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False


def get_number(token_list):
    n = token_list[0]
    if type(n) != type(0):
        return None
    del token_list[0]
    return Tree(n, None, None)


def get_operation(token_list):
    n = get_number(token_list)
    if get_token(token_list, '+'):
        m = get_operation(token_list)
        return Tree('+', n, m)
    return n


token_list = tokenize_list('(9 + 11) + (5 + 7)')
print(token_list)

tree = get_operation(token_list)
print_tree_postorder(tree)

