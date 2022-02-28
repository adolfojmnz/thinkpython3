import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def reverse(s):
    string = ''
    for i in s:
        string = i + string
    return string

def test_suite():
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")

test_suite()