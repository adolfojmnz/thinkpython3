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
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0}: OK.".format(linenum)
    else:
        msg = ("Test at line {0}: FAILED.".format(linenum))
    print(msg)


def total_secs(hours, minutes, seconds):
    return ((hours*3600) + (minutes * 60) + seconds)

def total_secs_int():
    return int ((hours*3600) + (minutes * 60) + seconds)

def suite_test_v7():
    test(total_secs(2, 30, 10) == 9010)
    test(total_secs(2, 0, 0) == 7200)
    test(total_secs(0, 2, 0) == 120)
    test(total_secs(0, 0, 42) == 42)
    test(total_secs(0, -10, 10) == -590)

def test_suite_v8():
    test(total_secs(2.5, 0, 10.71) == 9010)
    test(total_secs(2.433, 0, 0) == 8758)

suite_test_v7()
suite_test_v8()
