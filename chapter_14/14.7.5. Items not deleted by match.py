from unit_tester import test

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
                    xi+=1

                if first[xi] == second[yi]:
                    result.append(first[xi])               
        
        if first[xi] < second[yi]:
            result.append(first[xi])
            if xi+1 >= len(first):
                return result
            else: 
                xi+=1
                
        if first[xi] > second[yi]:
            if yi+1 >= len(second):
                result += first[xi:]
                return result
            else: 
                yi+=1


test(bagdiff([5,7,11,11,11,12,13], [7,8,11]) == [5,11,11,12,13])
test(bagdiff([7,8,11], [5,7,11,11,11,12,13]) == [8])
