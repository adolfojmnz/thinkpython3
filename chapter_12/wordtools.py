
def remove_occurs(old, new, string):
    """ 0) Removes all the occurences in a list. """
    result = ''
    for i, ch in enumerate(string):
        if string[i] == old:
            if string[i+1] == old:
                continue
        result += ch
    return new.join(result.split(old))


def cleanword(string):
    """ 1) Yields a string withow the below symbols. """
    result = ''
    symbols = ("-°|¬!$'%&/()=?\¡¿@+*~[{}]_:;.,><0123456789")
    for s in string:
        if s not in symbols:
            result += s
    return result


def has_dashdash(string):
    """ 2) Yields True if the string contains "--" (dash_dash). """
    if string.find('--') != -1:
        return True
    else:
        return False


def extract_words(string):
    """ 4. Extracts all the words from a string and yields them as a list. """
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # English ABC
    ABC_abc = ABC + ABC.casefold() + ' '
    for i in string:
        if i not in ABC_abc:
            string = string.replace(i, ' ')
    return string.casefold().split()


def wordcount(_string, _list):
    """ 4) Counts how many _string are present in _list. """
    count = 0
    for string in _list:
        if string == _string:
            count += 1
    return count


def wordset(_list):
    """ 5) Sort alphabetic the string list and delete the repeated ones. """
    _list.sort()
    result = []
    for string in _list:
        if string not in result:
            result.append(string)
    return result


def longestword(_list):
    """ 6) Find the longest word present in a list and returns its lenght. """
    result = 0
    for string in _list:
        if len(string) > result:
            result = len(string)
    return result
