from unit_tester import test

def wordset(_list):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abc = ABC.casefold()
    result = []
    for _string in _list:
        print(_string[0])
        if _string[0] in ABC:
            result.append(_string)
        elif _string in abc:
            result.append(_string)
    return result

#print(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]))