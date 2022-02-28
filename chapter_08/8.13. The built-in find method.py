import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print("Test at line {0} is OK.".format(line_num))
    else: print("Test at line {0} has FAILED.".format(line_num))


ss = "Python strings have some interesting methods."

test(ss.find("s") == 7)
test(ss.find("s", 7) == 7)
test(ss.find("s", 8) == 13)
test(ss.find("s", 8, 13) == -1) # Failure
test(ss.find(".") == len(ss)-1) # Failure
