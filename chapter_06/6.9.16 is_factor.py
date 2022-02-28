import sys


def test(x):
    z = sys._getframe(1).f_lineno
    if x:
       print(("Test at line {0} is OK.").format(z))
    else:
         print(("Test at line {0} has FAILED.").format(z))


def test_suite_v16():
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))


def test_suite_v17():
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))


def is_factor(f, n):
    if n % f == 0:
        return True
    else:
         return False


def is_multiple(m, x):
    return (is_factor(x, m))


# test_suite_v16()
# test_suite_v17()