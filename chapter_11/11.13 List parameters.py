
def double_stuff(a_list):
    for (idx, val) in enumerate(a_list):
        a_list[idx] = val*2

things = [2, 5, 9]
double_stuff(things)
print(things)