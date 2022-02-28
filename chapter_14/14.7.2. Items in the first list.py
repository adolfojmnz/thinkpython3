from unit_tester import test

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

test(merge([2], [1, 3, 4]) == [2])
test(merge([3, 5, 7], []) == [3, 5, 7])
test(merge([2, 4, 6, 8], [1, 3, 4, 6, 9]) == [2, 8])
test(merge([3, 6, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == [])
test(merge([1, 3, 4, 6, 8, 9], [2, 4, 6, 8]) == [1, 3, 9])
