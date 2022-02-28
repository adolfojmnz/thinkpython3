import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def mirror_strings(s):
    string = ''
    for i in s:
        string = i + string
    return s+string

def test_suite():
    test(mirror_strings("good") == "gooddoog")
    test(mirror_strings("Python") == "PythonnohtyP")
    test(mirror_strings("") == "")
    test(mirror_strings("a") == "aa")


test_suite()
