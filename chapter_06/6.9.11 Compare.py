#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Adolfo Jimenez
#
# Created:     23/06/2020
# Copyright:   (c) Adolfo Jimenez 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys


def test(did_pass):
    """print the result of a test."""
    linenum = sys._getframe(1).f_lineno
    if did_pass:
       msg = "Test at line {0} OK.".format(linenum)
    else:
         msg = ("Test at line {0} FAILED.").format(linenum)
    print(msg)


def test_suite_v11():
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

def compare(a, b):
    if a > b:
       return 1
    if a == b:
       return 0
    if a < b:
       return -1

test_suite_v11()
