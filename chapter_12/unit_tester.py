import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {linenum} is OK.')
    else: 
        print(f'Test at line {linenum} has FAILED.')

