def search_linear(xs, target):
    """ Find and return the index of target in sequence xs. """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1
