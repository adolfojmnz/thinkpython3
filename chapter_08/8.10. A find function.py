def find(string, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(string):
        if string[ix] == ch:
            return ix
        ix += 1
    return -1

print(find("Compsci", "p") == 3)
print(find("Compsci", "C") == 0)
print(find("Compsci", "i") == 6)
print(find("Compsci", "x") == -1)
