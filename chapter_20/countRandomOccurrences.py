from random import Random
from pprint import pprint

def find_occurrences(rng):
    output = {}
    for _ in range(0, 5000):
        random = rng.randint(0, 1000000000)      # Generates random numbers from 0 to 1 billion.
        output[random] = output.get(random, 0) + 1
    return output

rng = Random()
pprint(find_occurrences(rng))
