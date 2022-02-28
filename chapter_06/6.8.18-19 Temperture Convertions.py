import sys


def test(x):
    z = sys._getframe(1).f_lineno
    if x:
       print(("Test at line {0} is OK.").format(z))
    else:
         print(("Test at line {0} has FAILED.").formar(z))


def test_suite_v18():
    test(farenheint_to_celcius(212) == 100)
    test(farenheint_to_celcius(32) == 0)
    test(farenheint_to_celcius(-40) == -40)
    test(farenheint_to_celcius(36) == 2)
    test(farenheint_to_celcius(37) == 3)
    test(farenheint_to_celcius(38) == 3)
    test(farenheint_to_celcius(39) == 4)


def test_suite_v19():
    test(celcius_to_farenheint(0) == 32)
    test(celcius_to_farenheint(100) == 212)
    test(celcius_to_farenheint(-40) == -40)
    test(celcius_to_farenheint(12) == 54)
    test(celcius_to_farenheint(18) == 64)
    test(celcius_to_farenheint(-48) == -54)


def farenheint_to_celcius(t):
    return(round( 5/9 *(t-32)))


def celcius_to_farenheint(t):
    return(round(9/5 * t) + 32)


test_suite_v18()
test_suite_v19()
