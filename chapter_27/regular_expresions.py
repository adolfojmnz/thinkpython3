import re

def tokenize_list(string):
    ss = re.split('', string)
    for (i,v) in enumerate(ss):
        if v in ['(', ')']:
            del ss[i]
    ss = re.split(' ', ''.join(ss))
    return ss


s = '(9 * 11) + (5 * 7)'
print(tokenize_list(s))
