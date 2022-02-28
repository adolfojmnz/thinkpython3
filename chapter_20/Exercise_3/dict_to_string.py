from longest_in_dict import longest_key, longest_value


def dict_to_string(some_dict):
    key_lenght = len(longest_key(some_dict))
    value_lenght = len(str(longest_value(some_dict)))
    
    some_list = []

    for key in some_dict:
        to_append = f'{str(key).ljust(key_lenght + 1)} {str(some_dict[key]).rjust(value_lenght)}\n'
        some_list.append(to_append)

    SS = ''.join(some_list)
    return SS
