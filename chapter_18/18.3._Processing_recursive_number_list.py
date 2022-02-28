def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

a_list = [0, 1, 2, 3, 4, [5, 6, 7, 8], 9]
print(r_sum(a_list))
