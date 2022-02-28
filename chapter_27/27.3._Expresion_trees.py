from Tree import Tree

tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

def print_tree(tree):
    if tree is None:
        return
    print(tree.cargo, end=' ')
    print_tree(tree.left)
    print_tree(tree.right)

def print_indented(tree, level=0):
    if tree is None:
        return
    print_indented(tree.right, level+1)
    print('  ' * level + str(tree.cargo))
    print_indented(tree.left, level+1)

print_indented(tree)
