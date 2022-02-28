import random


rng = random.Random()

def List_without_dupplications(start, stop, steps, size):
    result = []
    list_size = (stop - start) // steps
    while len(result) < list_size:
        for _ in range(size):
            x = rng.randrange(start, stop, steps)
            if x not in result:
                result.append(x)
    return result

print(List_without_dupplications(1, 10, 2, 15))
