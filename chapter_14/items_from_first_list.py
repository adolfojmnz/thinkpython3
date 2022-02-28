def merge(first, second):
    xi = 0
    yi = 0
    result = []
    while True:
        condition = None

        if xi >= len(first):
            return result
        elif yi >= len(second):
            result += first[xi:]
            return result

        if first[xi] == second[yi]:
            if xi+1 >= len(first):
                return result
            else:
                xi += 1
            if yi+1 >= len(second):
                result += first[xi:]
                return result
            else:
                yi += 1

        if first[xi] < second[yi]:
            result.append(first[xi])
            xi += 1
            if xi >= len(first):
                return result

        elif first[xi] > second[yi]:
            while condition == None:
                if yi >= len(second):
                    result += first[xi:]
                    return result
                else:
                    yi += 1
                if first[xi] <= second[yi]:
                    condition = True
