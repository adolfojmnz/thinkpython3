def find2(string, ch, start):
    ix = start
    while ix < len(string):      #print('Starting...')
        if string[ix] == ch:     #print('Found in position', ix)
            return ix
        ix += 1                   #print('Ended!')
    return -1

def default_find(string, ch, start = 0, end=None):
    ix = start
    if end is None:
        end = len(string)
    while ix < end:
        if string[ix] == ch:
            #print("Character '{0}' was found in position '{1}'".format(ch, ix))
            return ix
        ix += 1
    #print("Character '{0}' wasn't found".format(ch))
    return -1

ss = "Python strings have some interesting methods."
def print_default():
    print(default_find(ss, "s") == 7)
    print(default_find(ss, "s", 7) == 7)
    print(default_find(ss, "s", 8) == 13)
    print(default_find(ss, "s", 8, 13) == -1)
    print(default_find(ss, ".") == len(ss)-1)

print(find2(ss, '?', 0) == -1)