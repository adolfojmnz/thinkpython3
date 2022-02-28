import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def count_substrings(substring, string):
    pos = 0
    count = 0
    while string.find(substring, pos) != -1:
        pos += string.find(substring, pos) + 2
        count += 1
    return count

def test_suite():
    test(count_substrings("is", "Mississippi") == 2)
    test(count_substrings("an", "banana") == 2)
    test(count_substrings("ana", "banana") == 2)
    test(count_substrings("nana", "banana") == 1)
    test(count_substrings("nanan", "banana") == 0)
    test(count_substrings("aaa", "aaaaaa") == 2) # [...] == 3

test_suite()
#print(count_substrings("aaa", "aaaaaa"))