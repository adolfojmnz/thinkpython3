def search_linear(xs, target):
    """ Find and return the index of target in sequence xs. """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1

    
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
print(search_linear(friends, "Zoe") == 1)
print(search_linear(friends, "Joe") == 0)
print(search_linear(friends, "Paris") == 6)
print(search_linear(friends, "Bill") == -1)

