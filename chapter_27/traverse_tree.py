from Tree import Tree

def add_tree(cargo, attr):
    if animals.__contains__(cargo):
        if attr not in (animals[cargo]):
            animals[cargo].append(attr)
            return 'Attribute appended'
        return 'The attribute alredy exist'
    animals[cargo] = [attr]
    return 'Cargo appended'

def traverse_tree(tree, attr):
    if tree is None: return
    traverse_tree(tree.left, attr)
    add_tree(tree.cargo, attr)
    traverse_tree(tree.right, attr)


def yes(answer):
    if answer[0].lower() == 'y':
        return True
    return False

def animal():
    animals = {}
    root = Tree('Bird')
    add_tree(root, [])

    while True:
        prompt = '\nAre you thinking on an animal? '
        if not yes(prompt):
            break

        tree = root
        while tree.left is not None:
            pass

        prompt = '\nWhat\'s the animal\'s name? '
        animal = input(prompt).lower().capitalize()

        add = 'a'
        if animal[0].lower() in 'aeiou':
            add = 'an'

        guess = tree.cargo
        prompt = f'\nWhat attribute distinguish {add} {animal} from {guess}'
        attribute = input(prompt).lower().capitalize()

        prompt = f'\nSo, if the animal were {add} {animal} it will posses such attribute? '
        new_animal = Tree(animal)

        if yes(prompt):
            pass


        # Add the new animal and its attribute.



