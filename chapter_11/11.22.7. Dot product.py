def dot_product(u, v):
    _v = 0
    for i in range(len(u)):
        _v += u[i] * v[i]
    return _v
    
print(dot_product([1, 1], [1, 1]) ==  2)
print(dot_product([1, 2], [1, 4]) ==  9)
print(dot_product([1, 2, 1], [1, 4, 3]) == 12)