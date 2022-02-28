def bagdiff(first, second):
    (xi, yi) = (0, 0)
    result = []

    while True:
        if xi >= len(first):
            return result
        if yi >= len(second):
            return result

        if first[xi] == second[yi]:
            while first[xi] == second[yi]:

                if xi+1 >= len(first):
                    return result
                else:
                    xi += 1

                if first[xi] == second[yi]:
                    result.append(first[xi])

        if first[xi] < second[yi]:
            result.append(first[xi])
            if xi+1 >= len(first):
                return result
            else:
                xi += 1

        if first[xi] > second[yi]:
            if yi+1 >= len(second):
                result += first[xi:]
                return result
            else:
                yi += 1

