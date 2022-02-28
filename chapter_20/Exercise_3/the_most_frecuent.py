def frecuency(some_dict):
    value = 0
    for k in some_dict:
        if value == 0 or some_dict[k] > value:
            value = some_dict[k]
            key = k
    return key, value
