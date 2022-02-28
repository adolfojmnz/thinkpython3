from unit_tester import test
from time import time

def merge(first, second):
    """ Returns only thoes elements that are present in both lists. """
    
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(first):           # If first list is finished
            return result
        if yi >= len(second):
            return result

        if first[xi] == second[yi]:
            result.append(first[xi])
            xi += 1
            yi += 1

        elif first[xi] < second[yi]:
            xi += 1

        elif first[xi] > second[yi]:
            yi += 1


xs = [1,2,3,4,5,6,7,8,9]
ys = [1,3,5,7,9,13,15]
zs = [1,3,5,7,9]

t0 = time()
test(merge(xs, ys) == zs)
t1 = time()
print(f'{t1-t0} seconds to run.')
