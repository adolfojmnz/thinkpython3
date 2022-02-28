def min(some_list):
    firstTime = True
    minimun = None
    try:
        for index in some_list:                             
            if type(some_list[index]) == type([]):
                minuimun = min(some_list[index])
            else:
                if firstTime or some_list[index] < minimun:
                    firstTime = False
                    minimun = some_list[index]
        return minimun 
    except:
        return minimun 


print(min([2, 9, [1, 13], 8, 6]))
