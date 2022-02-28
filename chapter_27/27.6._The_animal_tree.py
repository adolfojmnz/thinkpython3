from Tree import Tree


animals = {}
filename = '/home/adolfoj/Dev/thinkpython3/src/Chapter_27/animals.txt'
def get_animals(filename=filename):
    f = open(filename, 'r').readlines()
    for line in f:
        line = line.split(': ')
        if not animals.get(line[0], False):
            animals[line[0]] = line[1]
get_animals()

def add_animal(animal, attr):
    if not animals.get(animal, False):
        animals[animal] = f'{attr}\n'
        return True
    return False

def write_animal(animal, attr):
    if add_animal(animal, attr):
        to_write = f'{animal}: {attr}'
        open('animals.txt', 'w').write(to_write)
        return True
    return False

def create_tree(root='Bird'):
    tree = Tree(root)
    for key in animals.keys():
        pass


def yes(quest):
    ans = input(quest).lower()
    return ans[0] == 'y'

def animal():
    # Start with a singleton
    root = Tree('Bird')

    while True:
        if not yes('\nAre you thinking on an animal? '):
            print('break')
            break

        tree = root

        while tree.left is not None:
            prompt = f'Does the animal posses this attribute: {tree.cargo}? '
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        guess = tree.cargo
        prompt = f'Is it a {guess} ? '
        if yes(prompt):
            print('I rule!')
            continue

        prompt = 'What is the animal\'s name? '
        animal = input(prompt).lower().capitalize()

        add = 'a'
        if animal[0] in 'aeiou':
            add = 'an'

        prompt = f'What would be an attribute that distinguish {add} {animal} from {guess}? '
        attribute = input(prompt).lower().capitalize()

        # Add new information to the tree
        tree.cargo = attribute
        prompt = f'If the animal were {add} {animal}, will it posses such attribute? '
        if yes(prompt):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
            write_animal(animal, attribute)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            write_animal(guess, attribute)

animal()
