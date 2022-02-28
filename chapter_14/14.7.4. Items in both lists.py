from unit_tester import test

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


test(items_both_list([1,2,3,4,5], [2,3]) == [2,3])
test(items_both_list([2, 3, 4, 5], [1, 3, 5, 7]) == [3,5])
test(items_both_list([1,3,6,9], [1,2,3,4,5,6,7,8,9,10]) == [1,3,6,9])


