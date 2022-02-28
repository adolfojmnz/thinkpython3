def longest(some_dict):
    """
        Returns the longest element in a dictionary.
    """
    lenght = 0
    for key in some_dict:
        if len(str(lenght)) == 0 or len(str(lenght)) < len(str(key)):
            lenght = key
    return lenght

s = 'string'
print(s.rjust(2+len(s)))
