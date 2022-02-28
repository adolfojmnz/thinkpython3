class Tree:

    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.cargo}'

def total(tree):
    if tree is None:
        return 0
    total_sum = tree.cargo + total(tree.left) + total(tree.right)
    return total_sum


tree = Tree(1, Tree(3), Tree(2))
print(total(tree))
