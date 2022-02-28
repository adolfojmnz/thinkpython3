import sys


def test(x):
    z = sys._getframe(1).f_lineno
    if x:
       print("Test at line {0} is OK.".format(z))
    else:
         print("Test at line {0} has FAILED.".format(z))


def test_suite_v1():
    test(sum([1, 2, 3, 4]) == 10)
    test(sum([1.25, 2.5, 1.75]) == 5.5)
    test(sum([1, -2, 3]) == 2)
    test(sum([ ]) == 0)
    test(sum(range(11)) == 55)


def test_suite_v2():
    test(sum_to(4))
    test(sum_to(1000))


def sum(xs):
    total_sum = 0
    for v in xs:
        total_sum = total_sum + v
        print (total_sum)
        return total_sum


def sum_to(n):
    sum_n = 0
    v = 1
    while n >= v:
          sum_n = sum_n + v
          v = v + 1
    return sum_n


# test_suite_v1()
# test_suite_v2()
