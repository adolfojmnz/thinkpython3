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


def how_many_days(month):
    if month == "January":
       return 31
    if month == "February":
       return 28
    if month == "March":
       return 31
    if month == "April":
       return 30
    if month == "May":
       return 31
    if month == "June":
       return 30
    if month == "July":
       return 31
    if month == "August":
       return 31
    if month == "September":
       return 30
    if month == "Octuber":
       return 31
    if month == "November":
       return 30
    if month == "December":
       return 31
    else:
         return None


def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0}: OK.".format(linenum)
    else:
        msg = ("Test at line {0}: FAILED.".format(linenum))
    print(msg)


def suite_test_v6():
    test(how_many_days("February") == 28)
    test(how_many_days("December") == 31)


suite_test_v6()
