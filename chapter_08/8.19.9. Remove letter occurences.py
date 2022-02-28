import sys

def test(did_pass):
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        print(f'Test at line {line_num} is OK.')
    else: print(f'Test at line {line_num} has FAILED.')

def remove_occurrences(letter, string):
    new_string = ''
    for i in string:
        if i == letter:
            continue
        else:
            new_string = new_string + i
    return new_string

def test_suite():
    test(remove_occurrences('a', 'apple') == 'pple')
    test(remove_occurrences('a', 'banana') == 'bnn')
    test(remove_occurrences("i", "Mississippi") == "Msssspp")
    test(remove_occurrences("b", "") == "")
    test(remove_occurrences("b", "c") == "c")

test_suite()
