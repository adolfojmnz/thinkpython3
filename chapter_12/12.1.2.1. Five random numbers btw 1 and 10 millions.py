import random

def random_without_dups(num, lower_bound, upper_bound):
    """
        Generate a list containing num random ints between
        lower_bound and upper_bound. upper_bound is an open bound.
        The result list cannot contain duplicates.
      """
    x, result, rng = 0, [], random.Random()
    for _ in range(num):
        while True:
            if upper_bound - lower_bound == len(result):
                return result # If all the posible results have already been found.
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
    return result

#print(random_without_dups(5, 1, 10000000))

def random_numbers(num, lower_bound, upper_bound):
    """ This function do not always return a list of five elementes
    due to the posibillity of duplicate random numbers"""
    result, rng = [], random.Random()
    for _ in range(num):
        candidate = rng.randrange(lower_bound, upper_bound)
        if candidate in result:
            continue
        else:
            result.append(candidate)
    return result

print(random_numbers(5, 1, 10))
print(random_without_dups(10, 1, 6))


