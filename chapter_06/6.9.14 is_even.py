
import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
       msg = "Test at line {0} is Ok.".format(linenum)
    else:
         msg = "Test at line {0} has FAILED.".format(linenum)
    print(msg)


def test_suite_v14(n):
    print('Beggining "is even" test!')
    for i in range(2):
        if i == 0:
           print("Testing with", n)
        elif i == 1:
             print("Testing with", n)
        if n % 2 == 0:
           is_even(n)
        else:
           is_even(n)
        n = n+1


def test_suite_v15(n):
    print('Beggining "is odd" test!')
    for i in range(2):
        if i == 0:
           print("Testing with", n)
        if i == 1:
           print("Testing with", n)
        if n % 2 != 0:
            is_odd(n)
        else:
             is_odd(n)
        n = n+1


def is_even(n):
    if n % 2 == 0:
       print("The number is even")
       return True
    else:
         print("The number is odd")
         return False


def is_odd(n):
    if n % 2 != 0:
        print("The number is odd")
        return True
    else:
        print("The number is even")
        return False


def is_odd_v2(n):
    is_even(n)

test_suite_v15(6)
