def add_vectors(u, v):
    new_v = []
    for i in range(len(u)):
        _v = 0
        _v += u[i] + v[i]
        new_v.append(_v)
    return new_v

print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])