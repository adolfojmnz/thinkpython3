import sys


def area(radius):
    b = 3.141592 * radius ** 2
    return b


def absolute_value(x):
    if x < 0:
        return -x
    return x


def buggy_absolute_value(n):   # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n


def find_first_two_letters_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return ""


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))


def is_divisible_two(x, y):
    return x % y == 0


def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0}: OK.".format(linenum)
    else:
        msg = ("Test at line {0}: FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.141592) == 3.141592)


test_suite()
