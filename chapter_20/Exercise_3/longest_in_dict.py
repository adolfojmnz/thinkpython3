def longest_key(some_dict):
    """
        Returns the longest key in a dictionary.
    """
    lenght = 0
    for key in some_dict:
        if len(str(lenght)) == 0 or len(str(lenght)) < len(str(key)):
            lenght = key
    return lenght

def longest_value(some_dict):
    """
        Returns the longest value in a dictionary.
    """
    lenght = 0
    for value in some_dict.values():
        if len(str(lenght)) == 0 or len(str(lenght)) < len(str(value)):
            lenght = value
    return lenght
