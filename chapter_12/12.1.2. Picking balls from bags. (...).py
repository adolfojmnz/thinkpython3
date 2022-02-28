import random

def make_random_ints(num, lower_bound, upper_bound):
    """ Generae a list caontaining num random ints between
    lower_bound and upper_bound. upper_bound is an open bound.
    """
    rng = random.Random()
    result = []
    for _ in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result


# Random numbers from 1 to 12 without duplications.
rng = random.Random()
xs = list(range(1, 13))
rng.shuffle(xs) # Shuffle the list xd


print(make_random_ints(5, 1, 13))
print(xs[:5]) # Takes the first five elements.