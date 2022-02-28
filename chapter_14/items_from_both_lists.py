def items_both_list(first, second):
    xi = 0
    yi = 0
    result = []

    while True:
        if xi >= len(first):
            return result
        if yi >= len(second):
            return result

        if first[xi] == second[yi]:
            result.append(first[xi])
            if xi+1 >= len(first):
                return result
            else:
                xi += 1
            if yi+1 >= len(second):
                return result
            else:
                yi += 1

        else:
            if first[xi] > second[yi]:
                while first[xi] > second[yi]:
                    if yi+1 >= len(second):
                        return result
                    else:
                        yi += 1

            if first[xi] < second[yi]:
                if xi+1 >= len(first):
                    return result
                else:
                    xi += 1
