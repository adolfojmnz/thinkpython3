def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result. """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # add remaining items from ys.
            return result
        
        if yi >= len(ys):           # If xs list is finished,
            result.extend(xs[xi:])  # add remaining items from xs.
            return result

        # If both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else: 
            result.append(ys[yi])
            yi += 1